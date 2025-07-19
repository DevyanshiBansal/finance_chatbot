
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface.embeddings import HuggingFaceEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# loader = PyPDFLoader(r"C:\Users\devyanshi bansal\OneDrive\Documents\Module 1_Introduction to Stock Markets.pdf")
# pages = loader.load()

# # for chunks

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 1000,
#     chunk_overlap = 200
# )

# chunks = text_splitter.split_documents(pages)

# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
# db_path = r"C:\Users\devyanshi bansal\OneDrive\Documents\finance_chatbot\rag_folder"

# vectorstore = Chroma.from_documents(chunks, embedding=embedding_model, persist_directory=db_path)

# retriever = vectorstore.as_retriever()

# query = "what is crypto currency"
# docs = retriever.get_relevant_documents(query)

# for doc in docs:
#     print(doc.page_content)

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# Step 1: Load your PDF file
loader = PyPDFLoader(r"C:\Users\devyanshi bansal\OneDrive\Documents\Module 1_Introduction to Stock Markets.pdf")
documents = loader.load()

# Step 2: Split text into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Step 3: Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Step 4: Define your db_path (where to save vector DB)
db_path = r"C:\Users\devyanshi bansal\OneDrive\Documents\finance_chatbot\new_folder"

# Step 5: Create vector DB and persist
vector_db = Chroma.from_documents(documents=docs, embedding=embedding_model, persist_directory=db_path)
vector_db.persist()  # This saves it to disk
print("Vector DB created and saved!")