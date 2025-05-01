"""
Translate from OpenAI's `/v1/chat/completions` to Edenai's `/v2/llm/chat/completions`
"""

from ...openai_like.chat.handler import OpenAILikeChatConfig


class EdenaiChatConfig(OpenAILikeChatConfig):
    pass
