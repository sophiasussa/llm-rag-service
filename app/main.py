from fastapi import FastAPI
from app.modules.rag.presentation.rag_controller import router as rag_router

app = FastAPI(title="LLM RAG Service")

app.include_router(rag_router)
