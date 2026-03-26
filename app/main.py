from fastapi import FastAPI

app = FastAPI(title="LLM RAG Service")


@app.get("/")
def health_check():
    return {"status": "ok"}
