# def retrieve_psychological_context(query):
#     """Retrieve relevant psychological context from the vector database"""
#     if not vector_db:
#         print("No vector database available.")
#         return "No specific psychological information available."
    
#     try:
#         results = vector_db.similarity_search(query, k=2)  # API is the same for FAISS
#         context = "\n".join([f"- {doc.page_content[:300]}..." for doc in results])
#         return context
#     except Exception as e:
#         print(f"Error retrieving context: {str(e)}")
#         return "Unable to retrieve psychological context at this time."


# def load_vector_db():
#     '''load vector database pf financial content from Chroma'''
#     db_path = pdf_vector_db

#     if not os.path.exists(db_path):
#         print("ERROR")
#         return None
    
#     try:
#         print("loading vector database from Chroma...")
#         embeddding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

#         return Chroma(persist_directory=pdf_vector_db,embeddding_model=HuggingFaceEmbeddings)
    
#     except exception as e:
        
#         print(f"error loading chroma vector database: {str(e)}")
#         return None
    
        

# file = load_vector_db()

# def retrieve_content(query):
#     """used to retrieve financial content from vector database"""

#     if not file:
#         print("no vector database is available")
#         return None
    
#     try:
#         result = file.similarity_search(query,k=2)
#         context = "\n".join([f"- {doc.page_content[:300]}..." for doc in results])
#         return context
    
#     except Exception as e :
#         print(f"error retrieving content {str(e)}")
#         return "can't retrieve content right now"


from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.agents import Tool
import os
# load and retrieve

def load_vector_db():
    '''load the vector database'''

    db_path = r"C:\Users\devyanshi bansal\OneDrive\Documents\finance_chatbot\vector_store"

    if not os.path.exists(db_path):
        print("the vector database can't be loaded")
        return None
    
    try:

        embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        
        return Chroma(persist_directory=db_path, embedding_function=embeddings_model)
        
    except Exception as e:
        print(f"the vector database is not responding {str(e)}")
        return None
    

file = load_vector_db()

print(file)


def retrieve_content(query):
    '''used to retrieve financial content from vector database'''

    if not file:
        print("the file is empty")

    try:
        results = file.similarity_search(query, k=2)
        context = "\n".join([f"-{doc.page_content[:900]}..."for doc in results])

        return context
    
    except Exception as e:
        print(f"error retrieving content {str(e)}")
        return "can't retrieve content right now"
    

# this is just to check the programme
# query = "what is crypto currency"
# check = retrieve_content(query)
# print(check)

vector_tool = Tool(
    name = 'FinanceVectorDB',
    func = retrieve_content,
    description = "use this to retrieve knowledge related to finance from vector database."

)

