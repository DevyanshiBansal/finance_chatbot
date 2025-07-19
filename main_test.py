
import os
import getpass
from agent_file import get_agent
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


agent = get_agent()


# Step 1: Get API key
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = input("Enter your API key: ")

# Step 2: Define your custom prompt for Finance Assistant
prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are a helpful and professional *finance assistant*.
You only answer questions related to finance (e.g., investments, budgeting, crypto, markets, business strategy, etc.).
If the user asks anything *not related to finance*, politely say:
"I'm here to assist only with finance-related questions. Please ask me something about finance."

Conversation history:
{history}

User: {input}
Finance Assistant:"""
)

# Step 3: Set up memory and chain
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)  # or use ChatOpenAI for chat-style
memory = ConversationBufferMemory()

finance_chain = ConversationChain(
    llm=llm,
    prompt=prompt_template,
    memory=memory,
    verbose=True
)

# chat loop
while True:
   query = input("enter your question: ")
   response = finance_chain.run(query)
   print(response)
