# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="AI Chatbot API", version="1.0")

# Enable CORS for frontend
origins = [
    "http://localhost:5173",  # Vite dev server
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq API client
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Request model
class ChatRequest(BaseModel):
    user_id: str
    message: str

# In-memory chat memory
chat_memory = {}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        user_id = request.user_id
        user_message = request.message

        # Initialize memory for new user
        if user_id not in chat_memory:
            chat_memory[user_id] = []

        # Append user message
        chat_memory[user_id].append({"role": "user", "content": user_message})

        # Limit chat memory to last 20 messages
        MAX_HISTORY = 20
        chat_memory[user_id] = chat_memory[user_id][-MAX_HISTORY:]

        # Send chat history to AI
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=chat_memory[user_id]
        )
        ai_response = completion.choices[0].message.content

        # Append AI response
        chat_memory[user_id].append({"role": "assistant", "content": ai_response})

        return {"response": ai_response}

    except Exception as e:
        return {"error": str(e)}