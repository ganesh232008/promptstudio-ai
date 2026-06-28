from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.manager import process_request
from chat_memory import get_history, save_message

app = FastAPI(
    title="PromptForge AI",
    description="Multi-Agent Prompt Engineering Assistant",
    version="1.0.0"
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- Existing Prompt Request ----------------

class PromptRequest(BaseModel):
    idea: str


# ---------------- New Chat Request ----------------

class ChatRequest(BaseModel):
    session_id: str | None = None
    message: str


@app.get("/")
def home():
    return {
        "message": "Welcome to PromptForge AI 🚀",
        "status": "Running Successfully"
    }


# ---------------- Existing Endpoint ----------------

@app.post("/generate")
def create_prompt(request: PromptRequest):
    result = process_request(request.idea)
    return {
        "generated_prompt": result
    }


# ---------------- New Chat Endpoint ----------------

@app.post("/chat")
def chat(request: ChatRequest):

    session_id = request.session_id or str(uuid4())

    save_message(session_id, "user", request.message)

    history = get_history(session_id)

    reply = process_request(session_id, history)

    save_message(session_id, "assistant", reply)

    return {
        "session_id": session_id,
        "reply": reply
    }