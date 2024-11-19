# 環境変数の読み込み
import os
from typing import List

import chainlit as cl
import PyPDF2
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI  # ChatOpenAI をインポート
from langchain.docstore.document import Document
from langchain.embeddings.openai import \
    OpenAIEmbeddings  # OpenAI Embeddings をインポート
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS  # FAISS をインポート
# デポケーション警告を回避するためにインポートを更新
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()
api_key = os.getenv("Openai_api_key")

# テキスト分割の設定
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

@cl.on_chat_start
async def on_chat_start():
    files = None

    # ファイルアップロードを待機
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a PDF file to begin!",
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]
    print(f"Received file: {file.name}")

    msg = cl.Message(content=f"Processing {file.name}...")
    await msg.send()

    # PDFファイルの読み込み
    pdf = PyPDF2.PdfReader(file.path)
    pdf_text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            pdf_text += page_text

    # テキストをチャンクに分割
    texts = text_splitter.split_text(pdf_text)

    # 各チャンクにメタデータを追加
    metadatas = [{"source": f"{i}-page"} for i in range(len(texts))]

    # ベクターストアの初期化（FAISSを使用）
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)  # OpenAIEmbeddings を使用
    docsearch = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    # メモリの設定
    message_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )

    # RAGチェーンの作成
    chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(
            model_name="gpt-4",  # 必要に応じてモデルを指定
            openai_api_key=api_key,
            streaming=True,
        ),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        memory=memory,
        return_source_documents=True,
    )

    # セッションにチェーンを保存
    cl.user_session.set("chain", chain)

    # 処理完了メッセージ
    msg.content = f"Processing {file.name} done. You can now ask questions!"
    await msg.update()

@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")  # type: ConversationalRetrievalChain
    cb = cl.AsyncLangchainCallbackHandler()

    # チェーンにクエリを投げて結果を取得
    res = await chain.ainvoke(message.content, callbacks=[cb])
    answer = res["answer"]
    source_documents = res.get("source_documents", [])  # type: List[Document]

    text_elements = []  # type: List[cl.Text]

    # ソースドキュメントが存在する場合、参照元を追加
    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name)
            )
        source_names = [text_el.name for text_el in text_elements]

        if source_names:
            answer += f"\n\n**Sources:** {', '.join(source_names)}"
        else:
            answer += "\n**No sources found**"

    # 回答を送信
    await cl.Message(content=answer, elements=text_elements).send()
