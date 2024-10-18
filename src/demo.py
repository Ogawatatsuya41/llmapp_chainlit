import os

import chainlit as cl
from dotenv import load_dotenv
from openai import OpenAI

# .env ファイルから環境変数をロード
load_dotenv()

# OpenAI の API キーを設定
api_key = os.getenv("Openai_api_key")


client = OpenAI(api_key=api_key)
@cl.on_chat_start
async def start():
    await cl.Message(content='こんにちは！どのようなお手伝いができますか？').send()
settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 0.9,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.6,
    "stop": ["\n\n", "User:", "System:"]
}


@cl.on_message
async def main(message: cl.Message):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "あなたは親切で役立つアシスタントです。"},
            {"role": "user", "content": message.content}
        ],
        **settings
    )
    await cl.Message(content=str(response.choices[0].message.content)).send()
