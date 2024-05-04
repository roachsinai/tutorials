# generated by fastapi-codegen:
#   filename:  openai-openapi/openapi_modified.yaml
#   timestamp: 2024-05-04T14:14:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field, RootModel, confloat, conint


class Error(BaseModel):
    code: str
    message: str
    param: str
    type: str


class ErrorResponse(BaseModel):
    error: Error


class Object(Enum):
    list = "list"


class DeleteModelResponse(BaseModel):
    id: str
    deleted: bool
    object: str


class Model1(Enum):
    gpt_3_5_turbo_instruct = "gpt-3.5-turbo-instruct"
    davinci_002 = "davinci-002"
    babbage_002 = "babbage-002"


class PromptItem(RootModel):
    root: List[Any]


class CreateCompletionRequest(BaseModel):
    model: Union[str, Model1] = Field(
        ...,
        description="ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.\n",
    )
    prompt: Union[str, List[str], List[int], List[PromptItem]] = Field(
        ...,
        description="The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.\n\nNote that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.\n",
    )
    best_of: Optional[conint(ge=0, le=20)] = Field(
        1,
        description='Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.\n\nWhen used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.\n\n**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.\n',
    )
    echo: Optional[bool] = Field(
        False, description="Echo back the prompt in addition to the completion\n"
    )
    frequency_penalty: Optional[confloat(ge=-2.0, le=2.0)] = Field(
        0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.\n\n[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)\n",
    )
    logit_bias: Optional[Dict[str, int]] = Field(
        None,
        description='Modify the likelihood of specified tokens appearing in the completion.\n\nAccepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.\n\nAs an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.\n',
    )
    logprobs: Optional[conint(ge=0, le=5)] = Field(
        None,
        description="Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.\n\nThe maximum value for `logprobs` is 5.\n",
    )
    max_tokens: Optional[conint(ge=0)] = Field(
        16,
        description="The maximum number of [tokens](/tokenizer) that can be generated in the completion.\n\nThe token count of your prompt plus `max_tokens` cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.\n",
        example=16,
    )
    n: Optional[conint(ge=1, le=128)] = Field(
        1,
        description="How many completions to generate for each prompt.\n\n**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.\n",
        example=1,
    )
    presence_penalty: Optional[confloat(ge=-2.0, le=2.0)] = Field(
        0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.\n\n[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)\n",
    )
    seed: Optional[conint(ge=-9223372036854775808, le=9223372036854775807)] = Field(
        None,
        description="If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.\n\nDeterminism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.\n",
    )
    stop: Optional[Union[str, List[str]]] = Field(
        None,
        description="Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.\n",
    )
    stream: Optional[bool] = Field(
        False,
        description="Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).\n",
    )
    suffix: Optional[str] = Field(
        None,
        description="The suffix that comes after a completion of inserted text.\n\nThis parameter is only supported for `gpt-3.5-turbo-instruct`.\n",
        example="test.",
    )
    temperature: Optional[confloat(ge=0.0, le=2.0)] = Field(
        1,
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.\n\nWe generally recommend altering this or `top_p` but not both.\n",
        example=1,
    )
    top_p: Optional[confloat(ge=0.0, le=1.0)] = Field(
        1,
        description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.\n\nWe generally recommend altering this or `temperature` but not both.\n",
        example=1,
    )
    user: Optional[str] = Field(
        None,
        description="A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).\n",
        example="user-1234",
    )


class FinishReason(Enum):
    stop = "stop"
    length = "length"
    content_filter = "content_filter"


class Logprobs(BaseModel):
    text_offset: Optional[List[int]] = None
    token_logprobs: Optional[List[float]] = None
    tokens: Optional[List[str]] = None
    top_logprobs: Optional[List[Dict[str, float]]] = None


class Choice(BaseModel):
    finish_reason: FinishReason = Field(
        ...,
        description="The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,\n`length` if the maximum number of tokens specified in the request was reached,\nor `content_filter` if content was omitted due to a flag from our content filters.\n",
    )
    index: int
    logprobs: Logprobs
    text: str


class Object1(Enum):
    text_completion = "text_completion"


class Type(Enum):
    image_url = "image_url"


class Detail(Enum):
    auto = "auto"
    low = "low"
    high = "high"


class ImageUrl(BaseModel):
    url: AnyUrl = Field(
        ..., description="Either a URL of the image or the base64 encoded image data."
    )
    detail: Optional[Detail] = Field(
        "auto",
        description="Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision/low-or-high-fidelity-image-understanding).",
    )


class ChatCompletionRequestMessageContentPartImage(BaseModel):
    type: Type = Field(..., description="The type of the content part.")
    image_url: ImageUrl


class Type1(Enum):
    text = "text"


class ChatCompletionRequestMessageContentPartText(BaseModel):
    type: Type1 = Field(..., description="The type of the content part.")
    text: str = Field(..., description="The text content.")


class Role(Enum):
    system = "system"


class ChatCompletionRequestSystemMessage(BaseModel):
    content: str = Field(..., description="The contents of the system message.")
    role: Role = Field(
        ..., description="The role of the messages author, in this case `system`."
    )
    name: Optional[str] = Field(
        None,
        description="An optional name for the participant. Provides the model information to differentiate between participants of the same role.",
    )


class Role1(Enum):
    user = "user"


class Role2(Enum):
    assistant = "assistant"


class FunctionCall(BaseModel):
    arguments: str = Field(
        ...,
        description="The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.",
    )
    name: str = Field(..., description="The name of the function to call.")


class Role3(Enum):
    tool = "tool"


class ChatCompletionRequestToolMessage(BaseModel):
    role: Role3 = Field(
        ..., description="The role of the messages author, in this case `tool`."
    )
    content: str = Field(..., description="The contents of the tool message.")
    tool_call_id: str = Field(
        ..., description="Tool call that this message is responding to."
    )


class Role4(Enum):
    function = "function"


class ChatCompletionRequestFunctionMessage(BaseModel):
    role: Role4 = Field(
        ..., description="The role of the messages author, in this case `function`."
    )
    content: str = Field(..., description="The contents of the function message.")
    name: str = Field(..., description="The name of the function to call.")


class FunctionParameters(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ChatCompletionFunctions(BaseModel):
    description: Optional[str] = Field(
        None,
        description="A description of what the function does, used by the model to choose when and how to call the function.",
    )
    name: str = Field(
        ...,
        description="The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.",
    )
    parameters: Optional[FunctionParameters] = None


class ChatCompletionFunctionCallOption(BaseModel):
    name: str = Field(..., description="The name of the function to call.")


class Type2(Enum):
    function = "function"


class FunctionObject(BaseModel):
    description: Optional[str] = Field(
        None,
        description="A description of what the function does, used by the model to choose when and how to call the function.",
    )
    name: str = Field(
        ...,
        description="The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.",
    )
    parameters: Optional[FunctionParameters] = None


class ChatCompletionToolChoiceOption1(Enum):
    none = "none"
    auto = "auto"
    required = "required"


class Function(BaseModel):
    name: str = Field(..., description="The name of the function to call.")


class ChatCompletionNamedToolChoice(BaseModel):
    type: Type2 = Field(
        ...,
        description="The type of the tool. Currently, only `function` is supported.",
    )
    function: Function


class Function1(BaseModel):
    name: str = Field(..., description="The name of the function to call.")
    arguments: str = Field(
        ...,
        description="The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.",
    )


class ChatCompletionMessageToolCall(BaseModel):
    id: str = Field(..., description="The ID of the tool call.")
    type: Type2 = Field(
        ...,
        description="The type of the tool. Currently, only `function` is supported.",
    )
    function: Function1 = Field(..., description="The function that the model called.")


class Function2(BaseModel):
    name: Optional[str] = Field(None, description="The name of the function to call.")
    arguments: Optional[str] = Field(
        None,
        description="The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.",
    )


class ChatCompletionMessageToolCallChunk(BaseModel):
    index: int
    id: Optional[str] = Field(None, description="The ID of the tool call.")
    type: Optional[Type2] = Field(
        None,
        description="The type of the tool. Currently, only `function` is supported.",
    )
    function: Optional[Function2] = None


class ChatCompletionRole(Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    tool = "tool"
    function = "function"


class Role5(Enum):
    assistant = "assistant"


class FunctionCall2(BaseModel):
    arguments: Optional[str] = Field(
        None,
        description="The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.",
    )
    name: Optional[str] = Field(None, description="The name of the function to call.")


class Role6(Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    tool = "tool"


class ChatCompletionStreamResponseDelta(BaseModel):
    content: Optional[str] = Field(
        None, description="The contents of the chunk message."
    )
    function_call: Optional[FunctionCall2] = Field(
        None,
        description="Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.",
    )
    tool_calls: Optional[List[ChatCompletionMessageToolCallChunk]] = None
    role: Optional[Role6] = Field(
        None, description="The role of the author of this message."
    )


class Model2(Enum):
    gpt_4_turbo = "gpt-4-turbo"
    gpt_4_turbo_2024_04_09 = "gpt-4-turbo-2024-04-09"
    gpt_4_0125_preview = "gpt-4-0125-preview"
    gpt_4_turbo_preview = "gpt-4-turbo-preview"
    gpt_4_1106_preview = "gpt-4-1106-preview"
    gpt_4_vision_preview = "gpt-4-vision-preview"
    gpt_4 = "gpt-4"
    gpt_4_0314 = "gpt-4-0314"
    gpt_4_0613 = "gpt-4-0613"
    gpt_4_32k = "gpt-4-32k"
    gpt_4_32k_0314 = "gpt-4-32k-0314"
    gpt_4_32k_0613 = "gpt-4-32k-0613"
    gpt_3_5_turbo = "gpt-3.5-turbo"
    gpt_3_5_turbo_16k = "gpt-3.5-turbo-16k"
    gpt_3_5_turbo_0301 = "gpt-3.5-turbo-0301"
    gpt_3_5_turbo_0613 = "gpt-3.5-turbo-0613"
    gpt_3_5_turbo_1106 = "gpt-3.5-turbo-1106"
    gpt_3_5_turbo_0125 = "gpt-3.5-turbo-0125"
    gpt_3_5_turbo_16k_0613 = "gpt-3.5-turbo-16k-0613"


class Type6(Enum):
    text = "text"
    json_object = "json_object"


class ResponseFormat(BaseModel):
    type: Optional[Type6] = Field(
        "text",
        description="Must be one of `text` or `json_object`.",
        example="json_object",
    )


class FunctionCall3(Enum):
    none = "none"
    auto = "auto"


class FinishReason1(Enum):
    stop = "stop"
    length = "length"
    tool_calls = "tool_calls"
    content_filter = "content_filter"
    function_call = "function_call"


class Object2(Enum):
    chat_completion = "chat.completion"


class FinishReason2(Enum):
    stop = "stop"
    length = "length"
    function_call = "function_call"
    content_filter = "content_filter"


class TopLogprob(BaseModel):
    token: str = Field(..., description="The token.")
    logprob: float = Field(
        ...,
        description="The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.",
    )
    bytes: List[int] = Field(
        ...,
        description="A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.",
    )


class ChatCompletionTokenLogprob(BaseModel):
    token: str = Field(..., description="The token.")
    logprob: float = Field(
        ...,
        description="The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.",
    )
    bytes: List[int] = Field(
        ...,
        description="A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.",
    )
    top_logprobs: List[TopLogprob] = Field(
        ...,
        description="List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.",
    )


class Logprobs2(BaseModel):
    content: List[ChatCompletionTokenLogprob] = Field(
        ...,
        description="A list of message content tokens with log probability information.",
    )


class FinishReason3(Enum):
    stop = "stop"
    length = "length"
    tool_calls = "tool_calls"
    content_filter = "content_filter"
    function_call = "function_call"


class Choice3(BaseModel):
    delta: ChatCompletionStreamResponseDelta
    logprobs: Optional[Logprobs2] = Field(
        None, description="Log probability information for the choice."
    )
    finish_reason: FinishReason3 = Field(
        ...,
        description="The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,\n`length` if the maximum number of tokens specified in the request was reached,\n`content_filter` if content was omitted due to a flag from our content filters,\n`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.\n",
    )
    index: int = Field(
        ..., description="The index of the choice in the list of choices."
    )


class Object4(Enum):
    chat_completion_chunk = "chat.completion.chunk"


class CreateChatCompletionStreamResponse(BaseModel):
    id: str = Field(
        ...,
        description="A unique identifier for the chat completion. Each chunk has the same ID.",
    )
    choices: List[Choice3] = Field(
        ...,
        description="A list of chat completion choices. Can be more than one if `n` is greater than 1.",
    )
    created: int = Field(
        ...,
        description="The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.",
    )
    model: str = Field(..., description="The model to generate the completion.")
    system_fingerprint: Optional[str] = Field(
        None,
        description="This fingerprint represents the backend configuration that the model runs with.\nCan be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.\n",
    )
    object: Object4 = Field(
        ..., description="The object type, which is always `chat.completion.chunk`."
    )


class CreateChatCompletionImageResponse(BaseModel):
    pass


class Object5(Enum):
    model = "model"


class Model(BaseModel):
    id: str = Field(
        ...,
        description="The model identifier, which can be referenced in the API endpoints.",
    )
    created: int = Field(
        ..., description="The Unix timestamp (in seconds) when the model was created."
    )
    object: Object5 = Field(
        ..., description='The object type, which is always "model".'
    )
    owned_by: str = Field(..., description="The organization that owns the model.")


class CompletionUsage(BaseModel):
    completion_tokens: int = Field(
        ..., description="Number of tokens in the generated completion."
    )
    prompt_tokens: int = Field(..., description="Number of tokens in the prompt.")
    total_tokens: int = Field(
        ...,
        description="Total number of tokens used in the request (prompt + completion).",
    )


class Event(Enum):
    error = "error"


class ErrorEvent(BaseModel):
    event: Event
    data: Error


class Event1(Enum):
    done = "done"


class Data(Enum):
    field_DONE_ = "[DONE]"


class DoneEvent(BaseModel):
    event: Event1
    data: Data


class ListModelsResponse(BaseModel):
    object: Object
    data: List[Model]


class CreateCompletionResponse(BaseModel):
    id: str = Field(..., description="A unique identifier for the completion.")
    choices: List[Choice] = Field(
        ...,
        description="The list of completion choices the model generated for the input prompt.",
    )
    created: int = Field(
        ...,
        description="The Unix timestamp (in seconds) of when the completion was created.",
    )
    model: str = Field(..., description="The model used for completion.")
    system_fingerprint: Optional[str] = Field(
        None,
        description="This fingerprint represents the backend configuration that the model runs with.\n\nCan be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.\n",
    )
    object: Object1 = Field(
        ..., description='The object type, which is always "text_completion"'
    )
    usage: Optional[CompletionUsage] = None


class ChatCompletionRequestMessageContentPart(RootModel):
    root: Union[
        ChatCompletionRequestMessageContentPartText,
        ChatCompletionRequestMessageContentPartImage,
    ]


class ChatCompletionRequestUserMessage(BaseModel):
    content: Union[str, List[ChatCompletionRequestMessageContentPart]] = Field(
        ..., description="The contents of the user message.\n"
    )
    role: Role1 = Field(
        ..., description="The role of the messages author, in this case `user`."
    )
    name: Optional[str] = Field(
        None,
        description="An optional name for the participant. Provides the model information to differentiate between participants of the same role.",
    )


class ChatCompletionTool(BaseModel):
    type: Type2 = Field(
        ...,
        description="The type of the tool. Currently, only `function` is supported.",
    )
    function: FunctionObject


class ChatCompletionToolChoiceOption(RootModel):
    root: Union[ChatCompletionToolChoiceOption1, ChatCompletionNamedToolChoice] = Field(
        ...,
        description='Controls which (if any) tool is called by the model.\n`none` means the model will not call any tool and instead generates a message.\n`auto` means the model can pick between generating a message or calling one or more tools.\n`required` means the model must call one or more tools.\nSpecifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.\n\n`none` is the default when no tools are present. `auto` is the default if tools are present.\n',
    )


class ChatCompletionMessageToolCalls(RootModel):
    root: List[ChatCompletionMessageToolCall] = Field(
        ...,
        description="The tool calls generated by the model, such as function calls.",
    )


class ChatCompletionResponseMessage(BaseModel):
    content: str = Field(..., description="The contents of the message.")
    tool_calls: Optional[ChatCompletionMessageToolCalls] = None
    role: Role5 = Field(..., description="The role of the author of this message.")
    function_call: Optional[FunctionCall] = Field(
        None,
        description="Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.",
    )


class Choice1(BaseModel):
    finish_reason: FinishReason1 = Field(
        ...,
        description="The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,\n`length` if the maximum number of tokens specified in the request was reached,\n`content_filter` if content was omitted due to a flag from our content filters,\n`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.\n",
    )
    index: int = Field(
        ..., description="The index of the choice in the list of choices."
    )
    message: ChatCompletionResponseMessage
    logprobs: Logprobs2 = Field(
        ..., description="Log probability information for the choice."
    )


class CreateChatCompletionResponse(BaseModel):
    id: str = Field(..., description="A unique identifier for the chat completion.")
    choices: List[Choice1] = Field(
        ...,
        description="A list of chat completion choices. Can be more than one if `n` is greater than 1.",
    )
    created: int = Field(
        ...,
        description="The Unix timestamp (in seconds) of when the chat completion was created.",
    )
    model: str = Field(..., description="The model used for the chat completion.")
    system_fingerprint: Optional[str] = Field(
        None,
        description="This fingerprint represents the backend configuration that the model runs with.\n\nCan be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.\n",
    )
    object: Object2 = Field(
        ..., description="The object type, which is always `chat.completion`."
    )
    usage: Optional[CompletionUsage] = None


class Choice2(BaseModel):
    finish_reason: FinishReason2 = Field(
        ...,
        description="The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, or `function_call` if the model called a function.\n",
    )
    index: int = Field(
        ..., description="The index of the choice in the list of choices."
    )
    message: ChatCompletionResponseMessage


class CreateChatCompletionFunctionResponse(BaseModel):
    id: str = Field(..., description="A unique identifier for the chat completion.")
    choices: List[Choice2] = Field(
        ...,
        description="A list of chat completion choices. Can be more than one if `n` is greater than 1.",
    )
    created: int = Field(
        ...,
        description="The Unix timestamp (in seconds) of when the chat completion was created.",
    )
    model: str = Field(..., description="The model used for the chat completion.")
    system_fingerprint: Optional[str] = Field(
        None,
        description="This fingerprint represents the backend configuration that the model runs with.\n\nCan be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.\n",
    )
    object: Object2 = Field(
        ..., description="The object type, which is always `chat.completion`."
    )
    usage: Optional[CompletionUsage] = None


class ChatCompletionRequestAssistantMessage(BaseModel):
    content: Optional[str] = Field(
        None,
        description="The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.\n",
    )
    role: Role2 = Field(
        ..., description="The role of the messages author, in this case `assistant`."
    )
    name: Optional[str] = Field(
        None,
        description="An optional name for the participant. Provides the model information to differentiate between participants of the same role.",
    )
    tool_calls: Optional[ChatCompletionMessageToolCalls] = None
    function_call: Optional[FunctionCall] = Field(
        None,
        description="Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.",
    )


class ChatCompletionRequestMessage(RootModel):
    root: Union[
        ChatCompletionRequestSystemMessage,
        ChatCompletionRequestUserMessage,
        ChatCompletionRequestAssistantMessage,
        ChatCompletionRequestToolMessage,
        ChatCompletionRequestFunctionMessage,
    ]


class CreateChatCompletionRequest(BaseModel):
    messages: List[ChatCompletionRequestMessage] = Field(
        ...,
        description="A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).",
        min_items=1,
    )
    model: Union[str, Model2] = Field(
        ...,
        description="ID of the model to use. See the [model endpoint compatibility](/docs/models/model-endpoint-compatibility) table for details on which models work with the Chat API.",
        example="gpt-4-turbo",
    )
    frequency_penalty: Optional[confloat(ge=-2.0, le=2.0)] = Field(
        0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.\n\n[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)\n",
    )
    logit_bias: Optional[Dict[str, int]] = Field(
        None,
        description="Modify the likelihood of specified tokens appearing in the completion.\n\nAccepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.\n",
    )
    logprobs: Optional[bool] = Field(
        False,
        description="Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.",
    )
    top_logprobs: Optional[conint(ge=0, le=20)] = Field(
        None,
        description="An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.",
    )
    max_tokens: Optional[int] = Field(
        None,
        description="The maximum number of [tokens](/tokenizer) that can be generated in the chat completion.\n\nThe total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.\n",
    )
    n: Optional[conint(ge=1, le=128)] = Field(
        1,
        description="How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.",
        example=1,
    )
    presence_penalty: Optional[confloat(ge=-2.0, le=2.0)] = Field(
        0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.\n\n[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)\n",
    )
    response_format: Optional[ResponseFormat] = Field(
        None,
        description='An object specifying the format that the model must output. Compatible with [GPT-4 Turbo](/docs/models/gpt-4-and-gpt-4-turbo) and all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`.\n\nSetting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.\n\n**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.\n',
    )
    seed: Optional[conint(ge=-9223372036854775808, le=9223372036854775807)] = Field(
        None,
        description="This feature is in Beta.\nIf specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.\nDeterminism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.\n",
    )
    stop: Optional[Union[str, List[str]]] = Field(
        None,
        description="Up to 4 sequences where the API will stop generating further tokens.\n",
    )
    stream: Optional[bool] = Field(
        False,
        description="If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).\n",
    )
    temperature: Optional[confloat(ge=0.0, le=2.0)] = Field(
        1,
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.\n\nWe generally recommend altering this or `top_p` but not both.\n",
        example=1,
    )
    top_p: Optional[confloat(ge=0.0, le=1.0)] = Field(
        1,
        description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.\n\nWe generally recommend altering this or `temperature` but not both.\n",
        example=1,
    )
    tools: Optional[List[ChatCompletionTool]] = Field(
        None,
        description="A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.\n",
    )
    tool_choice: Optional[ChatCompletionToolChoiceOption] = None
    user: Optional[str] = Field(
        None,
        description="A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).\n",
        example="user-1234",
    )
    function_call: Optional[
        Union[FunctionCall3, ChatCompletionFunctionCallOption]
    ] = Field(
        None,
        description='Deprecated in favor of `tool_choice`.\n\nControls which (if any) function is called by the model.\n`none` means the model will not call a function and instead generates a message.\n`auto` means the model can pick between generating a message or calling a function.\nSpecifying a particular function via `{"name": "my_function"}` forces the model to call that function.\n\n`none` is the default when no functions are present. `auto` is the default if functions are present.\n',
    )
    functions: Optional[List[ChatCompletionFunctions]] = Field(
        None,
        description="Deprecated in favor of `tools`.\n\nA list of functions the model may generate JSON inputs for.\n",
        max_items=128,
        min_items=1,
    )
