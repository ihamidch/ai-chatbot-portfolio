from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# --- IMPORT YOUR BRAIN ---
from chatbot import YouTubeChatbot 
import uvicorn

app = FastAPI(title="YouTube AI Assistant")

class ChatRequest(BaseModel):
    url: str
    question: str

# Dictionary to store "sessions" so we don't reload the video 
# every time you ask a new question about the same link.
video_sessions = {}

@app.post("/chat")
async def chat_with_video(request: ChatRequest):
    try:
        # 1. Check if we already processed this video
        if request.url not in video_sessions:
            print(f"--- Processing new video: {request.url} ---")
            video_sessions[request.url] = YouTubeChatbot(request.url)
        
        # 2. Get the bot instance for this video
        bot = video_sessions[request.url]
        
        # 3. Ask the question and get a real AI answer
        answer = bot.ask(request.question)
        
        return {
            "video_url": request.url,
            "answer": answer,
            "status": "success"
        }
        
    except Exception as e:
        import traceback
        # THIS IS THE KEY: It prints the EXACT error to your VS Code terminal
        print("--- DATABASE/AI ERROR TRACEBACK ---")
        print(traceback.format_exc()) 
        print("------------------------------------")
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)