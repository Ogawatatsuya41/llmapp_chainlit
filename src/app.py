import chainlit as cl

import app_chain


@cl.on_chat_start
def on_chat_start():
    # チェーンをインスタンス化
    chain = app_chain.create_chain()

    # チェーンをセッションに保存
    cl.user_session.set("chain", chain)

@cl.on_message
async def on_message(message: cl.Message):
    query = message.content
    # チェーンをセッションから取得
    chain = cl.user_session.get("chain")

    # チェーンを呼び出し
    res = await chain.ainvoke({"input": query}, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # チェーンの応答を送信
    await cl.Message(content=res["text"]).send()