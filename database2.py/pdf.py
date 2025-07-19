
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# List your PDF files
pdf_paths = [
    r"C:\Users\devyanshi bansal\OneDrive\Documents\Module 1_Introduction to Stock Markets.pdf",
    r"C:\Users\devyanshi bansal\OneDrive\Documents\cryptocurrency.pdf"
]

# Step 1: Load and split all PDFs
all_docs = []
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)

for pdf in pdf_paths:
    loader = PyPDFLoader(pdf)
    pages = loader.load()
    chunks = text_splitter.split_documents(pages)
    all_docs.extend(chunks)

print(f"Loaded and split {len(all_docs)} chunks.")

# Step 2: Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Step 3: Define persist directory
db_path = r"C:\Users\devyanshi bansal\OneDrive\Documents\finance_chatbot\vector_store"

# Step 4: Build and save vector DB
vector_db = Chroma.from_documents(documents=all_docs, embedding=embedding_model, persist_directory=db_path)
vector_db.persist()

print("✅ All PDFs added and saved into vector DB.")