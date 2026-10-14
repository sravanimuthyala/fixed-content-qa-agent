import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from .prompts import SYSTEM_PROMPT

load_dotenv()


def create_qa_agent():
    llm = ChatGroq(
       model="openai/gpt-oss-20b",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ])

    chain = prompt | llm

    return chain
