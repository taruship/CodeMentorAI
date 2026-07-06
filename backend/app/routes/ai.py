from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.chat_history import ChatHistory

from app.schemas.code_generator import CodeRequest as GenerateRequest
from app.schemas.code_tools import CodeRequest

from app.services.ai_service import (
    ask_gemini,
    generate_code,
    explain_code,
    debug_code,
    review_code,
)

router = APIRouter()


# -----------------------
# Ask AI
# -----------------------
@router.get("/ask")
def ask(
    prompt: str,
    db: Session = Depends(get_db)
):
    answer = ask_gemini(prompt)

    chat = ChatHistory(
        prompt=prompt,
        response=answer
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return {
        "response": answer
    }


# -----------------------
# Generate Code
# -----------------------
@router.post("/generate-code")
def generate(request: GenerateRequest):

    result = generate_code(
        request.language,
        request.problem
    )

    return {
        "response": result
    }


# -----------------------
# Explain Code
# -----------------------
@router.post("/explain-code")
def explain(request: CodeRequest):

    result = explain_code(
        request.language,
        request.code
    )

    return {
        "response": result
    }


# -----------------------
# Debug Code
# -----------------------
@router.post("/debug-code")
def debug(request: CodeRequest):

    result = debug_code(
        request.language,
        request.code
    )

    return {
        "response": result
    }


# -----------------------
# Review Code
# -----------------------
@router.post("/review-code")
def review(request: CodeRequest):

    result = review_code(
        request.language,
        request.code
    )

    return {
        "response": result
    }
@router.get("/history")
def history(db: Session = Depends(get_db)):

    chats = db.query(ChatHistory).order_by(
        ChatHistory.id.desc()
    ).all()

    return chats
@router.delete("/history/{chat_id}")
def delete_history(
    chat_id: int,
    db: Session = Depends(get_db)
):
    chat = db.query(ChatHistory).filter(
        ChatHistory.id == chat_id
    ).first()

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat not found."
        )

    db.delete(chat)
    db.commit()

    return {
        "success": True,
        "message": f"Chat {chat_id} deleted successfully."
    }
@router.delete("/history")
def clear_history(db: Session = Depends(get_db)):

    db.query(ChatHistory).delete()

    db.commit()

    return {
        "success": True,
        "message": "All chat history deleted successfully."
    }