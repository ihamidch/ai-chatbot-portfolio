<<<<<<< HEAD
AI Chatbot Portfolio Project

Author: Hamid Rafique
Degree: BS Computer Science
Role: Portfolio-ready AI & Full-Stack Developer

Overview

This is a production-ready AI Chatbot built using FastAPI, Vue 3, and Groq LLM.
The chatbot supports:

Multi-turn conversations

Light/Dark mode

Long AI responses with proper line breaks

This project was completed as part of my 3-month roadmap for Generative AI & Agentic AI, covering Month 1.

Features

Backend API using FastAPI

Frontend UI built with Vue 3 + Bootstrap

Supports multi-user sessions with unique session IDs

Chat history memory stored on the backend

Light/Dark Mode toggle

Clear chat button

Proper line breaks for long AI responses

Fully responsive design for all screen sizes

Tech Stack

Backend: Python, FastAPI, Groq LLM

Frontend: Vue 3, Bootstrap, Axios

Environment Management: .env file for API keys

Setup & Run
Backend

Create a virtual environment:

python -m venv venv

Activate virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Add your Groq API key in a .env file:

GROQ_API_KEY=your_api_key_here

Run backend server:

python -m uvicorn main:app --reload
Frontend

Navigate to the frontend folder:

cd frontend

Install dependencies:

npm install

Run frontend dev server:

npm run dev

Open the app in your browser:

http://localhost:5173
Screenshot

Add your actual screenshot in screenshots/chat_interface.png.

Future Improvements

Deploy backend on Render/Railway and frontend on Vercel for a live demo

Add voice input/output for more interactive chat

Implement persistent chat storage using a database like PostgreSQL or MongoDB

Enhance chat UI with animations and emoji support

Live Demo (Optional)

Frontend: [Vercel link]

Backend: [Render/Railway link]

Replace placeholders with actual URLs once deployed.

✅ Summary

This project demonstrates your ability to build a full-stack AI application from scratch, integrating:

Modern backend with FastAPI & Groq LLM

Interactive frontend with Vue 3 + Bootstrap

Production-grade features like dark mode, multi-user sessions, chat memory, and responsive UI

Perfect for adding to your portfolio and resume.
=======
# ai-chatbot-portfolio
Production-ready AI Chatbot built with FastAPI, Vue 3, and Groq LLM.
>>>>>>> 008247f8696eeb6ba36b38017b510c65b334c94d

## Screenshot

![AI Chatbot UI](screenshots/chatbot.png)