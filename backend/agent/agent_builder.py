import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from .prompts import SYSTEM_PROMPT

load_dotenv()


def create_qa_agent():
     api_key = os.getenv("GROQ_API_KEY")

    print("GROQ KEY FOUND:", bool(api_key))
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ])

    chain = prompt | llm

    return chain
