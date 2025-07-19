
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader(r"C:\Users\devyanshi bansal\OneDrive\Documents\cryptocurrency.pdf")
pages = loader.load()

# for chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = text_splitter.split_documents(pages)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

db_path = r"C:\Users\devyanshi bansal\OneDrive\Documents\finance_chatbot\new_folder"

vectorstore = Chroma.from_documents(chunks,embedding=embedding_model,persist_directory=db_path)

# retriever = vectorstore.as_retriever()

# query = "what is crypto currency"
# docs = retriever.get_relevant_documents(query)

# for doc in docs:
#     print(doc.page_content)