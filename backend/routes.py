from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List

from services.docstore import doc_store
from agent.agent_builder import create_qa_agent

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    texts = []

    for file in files:
        content = await file.read()
        # Decode using utf-8 with error replacing to prevent crashing on odd characters
        texts.append(content.decode("utf-8", errors="ignore"))

    doc_store.add_texts(texts)

    return {
        "status": "success",
        "message": "Files uploaded and stored successfully."
    }


@router.post("/ask")
async def ask_question(req: QuestionRequest):
    # Retrieve context from doc_store
    context = doc_store.get_all_text()

    # Check for missing or blank context
    if not context or not context.strip():
        raise HTTPException(
            status_code=400, 
            detail="No documents found on server. Please upload your files again."
        )

    try:
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

    except Exception as e:
        # Catch internal failures (e.g., LLM API keys, timeout) and return HTTP 500
        # so CORS headers are preserved and sent back to the browser
        print(f"Error executing agent: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while processing the agent: {str(e)}"
        )
