import sys
# 1. THE "MONKEY PATCH" (Must be the very first thing)
try:
    import pytubefix as pytube
    sys.modules["pytube"] = pytube
except ImportError:
    # If pytubefix isn't installed, we catch it here
    pass

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class YouTubeChatbot:
    def __init__(self, url):
        self.url = url
        # HuggingFace handles the "Math" of the text
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        # Groq handles the "Brain" logic
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
        self.vector_store = self._build_memory()

    def _build_memory(self):
        # We use add_video_info=True because we fixed the pytube issue above
        loader = YoutubeLoader.from_youtube_url(self.url, add_video_info=True)
        docs = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_documents(docs)
        
        return FAISS.from_documents(chunks, self.embeddings)

    def ask(self, question):
        template = """Answer the question based ONLY on the following context:
        {context}
        
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        retriever = self.vector_store.as_retriever()

        # The LCEL "Pipe" Chain
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return chain.invoke(question)