# Chatbot デモプロジェクト

![Python](https://img.shields.io/badge/Language-Python-blue) ![OpenAI](https://img.shields.io/badge/OpenAI-API-blue) ![LangChain](https://img.shields.io/badge/LangChain-1.0.0-orange)

## 目次

- [はじめに](#はじめに)
- [特徴](#特徴)
- [前提条件](#前提条件)
- [インストール](#インストール)
- [使用方法](#使用方法)
  - [1. シンプルなOpenAIチャット (`api.py`)](#1-シンプルなopenaiチャット-apipy)
  - [2. LangChain統合 (`app_.py`と`app_chain.py`)](#2-langchain統合-appapyとapp_chainpy)
  - [3. LangChainを使用したOpenAI APIとの連携 (`lang.py`)](#3-langchainを使用したopenai-apiとの連携-langpy)
  - [4. PDF対応のRetrieval-Augmented Generation (RAG) (`rag.py`)](#4-pdf対応のretrieval-augmented-generation-ragpy)

---

## はじめに

Chatbot デモプロジェクトへようこそ！このリポジトリでは、OpenAIのAPIとLangChainを使用したさまざまなチャットボットの実装例を紹介しています。シンプルな会話型ボットから高度なLangChain統合、さらにPDFドキュメントを処理・クエリできるRetrieval-Augmented Generation (RAG) システムまで含まれています。

## 特徴

- **シンプルチャットボット (`api.py`)**: OpenAIのAPIを直接使用した基本的な会話機能。
- **LangChain統合 (`app_.py`と`app_chain.py`)**: LangChainを活用したより高度な会話機能。
- **強化されたLangChainボット (`lang.py`)**: LangChainを使用してOpenAIのAPIと連携し、対話管理を強化。
- **RAGシステム (`rag.py`)**: PDFドキュメントを処理し、その内容に基づいて質問に回答するRetrieval-Augmented Generationシステム。

## 前提条件

プロジェクトを始める前に、以下の条件を満たしていることを確認してください：

- **オペレーティングシステム**: Windows、macOS、またはLinux
- **Python**: バージョン3.8以上
- **Docker**（オプション、コンテナ化されたセットアップ用）

## インストール

### 1. リポジトリをクローン

```bash
git clone https://github.com/matsuoinstitute/chatbot-demo.git
cd chatbot-demo
```

### 2.VSCodeにて、cloneしてできたchatbot-demoフォルダを選択

> ![alt text](resource/fig/vscode_フォルダ選択.png)

### 3. env ファイルの設定

> 以下のような構造になっていれば OK です

> ![alt text](resource/fig/vscode_env.png)

env.sample をコピー＆ペーストして、作成できたファイルを「.env」という名前に変更

> 以下のような構造になっていれば OK です

> ![alt text](resource/fig/vscode_env.png)

.env ファイルには、「sk-」から始まる自分の OpenAI API キーを設定します。（step1 にて使用）

### 4. 右下に出てくる、「コンテナを再度開く」ボタンを押す

> ボタンが出てこない場合は、コマンドパレット（⌘+shift+p）を開けば、コンテナを開くボタンが出現します

> ![alt text](resource/fig/vscode_コマンドパレットでコンテナを再度開く.png)

---

## 使用方法

### [1. シンプルなOpenAIチャット (`api.py`)]

```py
# src直下に移動
cd src
```

```sh
# demo.pyを実行
chainlit run api.py -w
```

### [2. LangChain統合 (`app_.py`と`app_chain.py`)]

```py
# src直下に移動
cd src
```

```sh
# demo.pyを実行
chainlit run app.py -w
```

### [3. LangChainを使用したOpenAI APIとの連携 (`lang.py`)]

```py
# src直下に移動
cd src
```

```sh
# demo.pyを実行
chainlit run lang.py -w
```

### [4. PDF対応のRetrieval-Augmented Generation (RAG) (`rag.py`)]

```py
# src直下に移動
cd src
```

```sh
# demo.pyを実行
chainlit run rag.py -w
```