import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
index = faiss.read_index("index.faiss")

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

def search(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec).astype("float32"), k=3)
    return [chunks[i] for i in I[0]]

st.title("🤖 Website Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    results = search(prompt)
    combined = " ".join(results)

    answer = "\n".join([f"- {s.strip()}" for s in combined.split(". ")[:5]])

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)