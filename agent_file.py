
from T4 import duckduckgo_search_json_tool
from vectorDB_tool import vector_tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory

def get_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    tools = [duckduckgo_search_json_tool, vector_tool]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        agent_kwargs={
            "system_message": (
                "You are a helpful and professional finance assistant. "
                "Only answer finance-related questions like investments, crypto, budgeting, etc. "
                "If the user asks unrelated questions, politely decline. "
                "Maintain context of past conversations and answer accordingly."
            )
        },
        verbose=True  # optional
    )

    return agent


# from T4 import duckduckgo_search_json_tool
# from vectorDB_tool import vector_tool
# from langchain.agents import tool
# from langchain.agents import initialize_agent,AgentType
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# from langchain.prompts import PromptTemplate

# def get_agent():

#     llm = ChatGoogleGenerativeAI(
#     model = "gemini-2.0-flash",
#     temperature = 0,
#     max_tokens = None,
#     timeout = None,
#     max_retries = 2,
#     )

#     memory = ConversationBufferMemory(memory_key = "history", return_messages = True)

    
# # Step 2: Define your custom prompt for Finance Assistant
#     prompt_template = PromptTemplate(
#     input_variables=["history", "input"],
#     template="""
# You are a helpful and professional *finance assistant*.
# You only answer questions related to finance (e.g., investments, budgeting, crypto, markets, business strategy, etc.).
# If the user asks anything *not related to finance*, politely say:
# "I'm here to assist only with finance-related questions. Please ask me something about finance."

# Conversation history:
# {history}

# User: {input}
# Finance Assistant:"""

# )

#     tools = [duckduckgo_search_json_tool,vector_tool]

#     agent = initialize_agent(
#         tools = tools,
#         llm = llm,
#         agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
#         memory = memory,
#         agent_kwargs = {"system_message": prompt_template.template}
#         # verbose = True # it gives all the steps like how the model is thinking what it will do next and everything
#     )

#     return agent