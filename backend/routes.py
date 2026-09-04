from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional

from agent.agent_builder import create_qa_agent

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    context: Optional[str] = None


@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    texts = []
    for file in files:
        content = await file.read()
        texts.append(content.decode("utf-8", errors="ignore"))

    combined_text = "\n\n".join(texts)

    return {
        "status": "success",
        "message": "Files uploaded successfully.",
        "text": combined_text
    }


@router.post("/ask")
async def ask_question(req: QuestionRequest):
    if not req.context or not req.context.strip():
        raise HTTPException(
            status_code=400, 
            detail="No document text provided. Please upload your files again."
        )

    try:
        agent = create_qa_agent()

        result = agent.invoke({
            "input": f"""
Answer the question ONLY from the context below.

Context:
{req.context}

Question:
{req.question}
"""
        })

        return {"answer": result.content}

    except Exception as e:
        print(f"Error executing agent: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while processing the agent: {str(e)}"
        )
