
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader(r"C:\Users\devyanshi bansal\OneDrive\Documents\finance.pdf.pdf")
pages = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = Chroma.from_documents(pages, embedding=embedding_model, persist_directory="vector_db")

# retriever = vectorstore.as_retriever()

# query = "what is forecasting"
# docs = retriever.get_relevant_documents(query)

# for doc in docs:
#     print(doc.page_content)