import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="YouTube AI Assistant", page_icon="📺", layout="centered")

st.title("📺 YouTube Video Chatbot")
st.markdown("Paste a YouTube URL and ask questions about the video content.")

# 2. Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    api_url = st.text_input("Backend API URL", value="http://127.0.0.1:8000/chat")
    st.info("Ensure your FastAPI server is running!")

# 3. Input Section
video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input
if prompt := st.chat_input("What is this video about?"):
    if not video_url:
        st.error("Please enter a YouTube URL first!")
    else:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call FastAPI Backend
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    payload = {"url": video_url, "question": prompt}
                    response = requests.post(api_url, json=payload)
                    
                    if response.status_code == 200:
                        answer = response.json().get("answer", "No answer found.")
                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    else:
                        st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
                except Exception as e:
                    st.error(f"Connection failed: {e}") 