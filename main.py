
import os
import getpass
from agent_file import get_agent
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

# api_key = os.getenv("api_key")
# print(api_key)
 
if "GOOGLE_API_KEY" not in os.environ:
  os.environ["GOOGLE_API_KEY"] = input("enter your API key :")

agent= get_agent()

while True:
   query = input("enter your question: ")
   response = agent.run(query)
   print(response)
        

