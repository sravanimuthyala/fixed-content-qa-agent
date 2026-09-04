from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(title="Fixed Content Q&A Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fixed-content-qa-agent.netlify.app/",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
