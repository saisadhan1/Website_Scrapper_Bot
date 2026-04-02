import pandas as pd
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load data
df = pd.read_csv("data.csv")
texts = df["content"].tolist()

# Chunking
chunks = []
chunk_size = 3

for i in range(0, len(texts), chunk_size):
    chunk = " ".join(texts[i:i+chunk_size])
    chunks.append(chunk)

print("Chunks:", len(chunks))

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
embeddings = model.encode(chunks)

# Create FAISS index
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save
faiss.write_index(index, "index.faiss")

with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ Embedding + Index saved")