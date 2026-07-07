from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.ai import router as ai_router
from app.database.database import engine, Base
from app.models.chat_history import ChatHistory

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="CodeMentor AI",
    version="1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://code-mentor-ai-ruby.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to CodeMentor AI!"
    }

# Health Check
@app.get("/health")
def health():
    return {
        "status": "running"
    }

# Profile
@app.get("/profile")
def profile():
    return {
        "name": "Tarushi Pradhan",
        "project": "CodeMentor AI"
    }

# AI Routes
app.include_router(ai_router)