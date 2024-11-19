
import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains.base import Chain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

api_key = os.getenv("Openai_api_key")
api_key = SecretStr(api_key)
template = """関西弁に変換してください
変換前:{input}
変換後:"""


def create_chain() -> Chain:
    llm = ChatOpenAI(api_key=api_key, temperature=0, model="gpt-3.5-turbo", streaming=True)
    prompt = PromptTemplate(template=template, input_variables=["input"])
    return LLMChain(prompt=prompt, llm=llm, verbose=True)