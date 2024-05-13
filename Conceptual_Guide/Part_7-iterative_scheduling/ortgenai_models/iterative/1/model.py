# Copyright 2024, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import json
from pathlib import Path

import numpy as np
import onnxruntime_genai as og
import triton_python_backend_utils as pb_utils


class State:
    def __init__(self):
        self.prompt_tokens_len = 0
        self.tokens = []
        self.max_tokens = 0
        self.generator_params = None


class TritonPythonModel:
    def initialize(self, args):
        self.state = {}
        self.model_path = str(Path(args["model_repository"]) / args["model_version"])
        self.model = og.Model(self.model_path)
        self.tokenizer = og.Tokenizer(self.model)

    def create_batch(self, requests):
        """
        Create a batch of requests to be processed by the model.

        Args:
            requests (list): A list of Triton requests to process.

        Returns:
            og.GeneratorParams: A generator parameters object for the model.
        """
        generator_params = og.GeneratorParams(self.model)

        input_ids = []
        for request in requests:
            input_tensor = str(
                pb_utils.get_input_tensor_by_name(request, "text_input")
                .as_numpy()
                .item(),
                encoding="utf-8",
            )
            correlation_id = (
                pb_utils.get_input_tensor_by_name(request, "correlation_id")
                .as_numpy()
                .item()
            )
            start = (
                pb_utils.get_input_tensor_by_name(request, "start").as_numpy().item()
            )
            if start:
                state = State()
                state.tokens = self.tokenizer.encode(input_tensor)
                state.prompt_tokens_len = len(state.tokens)

                # Store the parameters
                parameters = json.loads(request.parameters())
                state.max_tokens = parameters["max_tokens"]

                self.state[correlation_id] = state
            state = self.state[correlation_id]
            input_ids.append(state.tokens)

        # Find the max sequence length
        max_len = max([len(x) for x in input_ids])
        input_ids = [
            [generator_params.pad_token_id] * (max_len - len(x)) + x for x in input_ids
        ]
        generator_params.input_ids = np.asarray(input_ids)

        return generator_params

    def send_responses(self, requests, outputs, generator_params):
        """
        Send responses for each request based on the model outputs and update
        the state of each request.

        Args:
            requests (list): A list of Triton requests to process.
            outputs (list): A list of generated tokens from the model for each request.
            generator_params (og.GeneratorParams): Parameters used for generating responses.
        """
        for i, request in enumerate(requests):
            correlation_id = (
                pb_utils.get_input_tensor_by_name(request, "correlation_id")
                .as_numpy()
                .item()
            )
            response_sender = request.get_response_sender()
            generated_token = outputs[i]

            # Maximum generated token length
            max_tokens = (
                self.state[correlation_id].max_tokens
                + self.state[correlation_id].prompt_tokens_len
            )

            self.state[correlation_id].tokens.append(outputs[i])
            if (outputs[i] == generator_params.eos_token_id) or len(
                self.state[correlation_id].tokens
            ) >= max_tokens:
                flags = pb_utils.TRITONSERVER_RESPONSE_COMPLETE_FINAL
                request.set_release_flags(pb_utils.TRITONSERVER_REQUEST_RELEASE_ALL)
                del self.state[correlation_id]
            else:
                request.set_release_flags(
                    pb_utils.TRITONSERVER_REQUEST_RELEASE_RESCHEDULE
                )
                flags = 0

            output_decoded = self.tokenizer.decode(generated_token)
            response = pb_utils.InferenceResponse(
                output_tensors=[
                    pb_utils.Tensor(
                        "text_output", np.array([output_decoded], dtype=np.object_)
                    )
                ]
            )
            response_sender.send(response, flags=flags)

    def execute(self, requests):
        generator_params = self.create_batch(requests)

        generator = og.Generator(self.model, generator_params)

        # Compute the logits and generate the next token
        generator.compute_logits()
        generator.generate_next_token()
        outputs = generator.get_next_tokens()

        # Send the responses for every request
        self.send_responses(requests, outputs, generator_params)
