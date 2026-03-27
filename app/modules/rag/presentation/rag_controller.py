from fastapi import APIRouter, UploadFile, File, Body

from app.modules.rag.application.text_splitter import split_text

router = APIRouter(prefix="/rag", tags=["rag"])


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return {
            "error": "File must be a UTF-8 encoded text file (.txt)"
        }

    chunks = split_text(text)

    return {
        "message": "document processed",
        "chunks": len(chunks)
    }


@router.post("/ask")
async def ask(question: str = Body(...)):
    return {
        "question": question,
        "answer": "not implemented yet"
    }
