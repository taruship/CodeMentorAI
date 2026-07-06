from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes.ai import router as ai_router
from app.services.ai_service import ask_gemini
from app.database.database import engine
from app.models.chat_history import ChatHistory
from app.database.database import Base
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="CodeMentor AI",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to CodeMentor AI!"}


@app.get("/health")
def health():
    return {"status": "running"}


@app.get("/profile")
def profile():
    return {
        "name": "Tarushi Pradhan",
        "project": "CodeMentor AI"
    }
app.include_router(ai_router)

