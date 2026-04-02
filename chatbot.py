import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load index
index = faiss.read_index("index.faiss")

# Load chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

def search(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec).astype("float32"), k=3)
    return [chunks[i] for i in I[0]]

print("🤖 Chatbot Ready! Type 'exit' to quit.\n")

while True:
    q = input("Ask: ")

    if q.lower() == "exit":
        break

    results = search(q)

    print("\n🔍 Answer:\n")

    combined = " ".join(results)
    sentences = combined.split(". ")

    for i, s in enumerate(sentences[:5], 1):
        print(f"{i}. {s.strip()}")

    print("\n" + "-"*50)