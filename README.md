# 🤖 YouTube AI Context Analyst (RAG)
A Full-Stack AI application that uses **Retrieval-Augmented Generation** to "chat" with any YouTube video.

### 🚀 Tech Stack
- **AI Orchestration:** LangChain (LCEL)
- **LLM:** Llama 3.3 (via Groq)
- **Vector Store:** FAISS
- **Backend:** FastAPI
- **Frontend:** Streamlit

### 🛠️ Setup
1. Clone the repo.
2. Create a `.venv` and run `pip install -r requirements.txt`.
3. Add your `GROQ_API_KEY` to a `.env` file.
4. Run `python main.py` and `streamlit run app.py`.
## 🏗️ Architecture
The system follows a decoupled **Microservices-style** architecture:
1. **Data Ingestion:** `YouTubeLoader` fetches transcripts via API.
2. **Vector Engine:** `HuggingFaceEmbeddings` + `FAISS` for high-speed semantic retrieval.
3. **Orchestration:** `LangChain (LCEL)` manages the prompt-to-model pipeline.
4. **Inference:** `Groq (Llama 3.3)` provides low-latency, high-accuracy responses.
5. **API Layer:** `FastAPI` handles asynchronous requests.
6. **UI:** `Streamlit` provides a real-time chat experience.