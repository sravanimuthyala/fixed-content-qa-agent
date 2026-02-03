from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel

from services.docstore import doc_store
from agent.agent_builder import create_qa_agent

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    texts = []

    for file in files:
        content = (await file.read()).decode("utf-8")
        texts.append(content)

    doc_store.add_texts(texts)

    return {
        "status": "success",
        "message": "Files uploaded and stored in memory."
    }


@router.post("/ask")
async def ask_question(req: QuestionRequest):
    context = doc_store.get_all_text()

    if not context:
        raise HTTPException(status_code=400, detail="No documents uploaded.")

    agent = create_qa_agent()

    result = agent.invoke({
        "input": f"""
Answer the question ONLY from the context below.

Context:
{context}

Question:
{req.question}
"""
    })

    return {"answer": result.content}
