# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from openapi_server.apis.chat_api import router as ChatApiRouter
from openapi_server.apis.completions_api import router as CompletionsApiRouter
from openapi_server.apis.models_api import router as ModelsApiRouter

app = FastAPI(
    title="OpenAI API",
    description="The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.",
    version="2.0.0",
)

app.include_router(ChatApiRouter)
app.include_router(CompletionsApiRouter)
app.include_router(ModelsApiRouter)
