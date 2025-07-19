from langchain_community.tools import DuckDuckGoSearchRun
import json
from langchain.agents import Tool

search = DuckDuckGoSearchRun()

def duckduckgo_search_json():
    
    query = "current stock price of tesla"
    result = search.invoke(query)

    json_result = json.dumps({
      "query": query,
      "result": result
    }, indent = 2)

    return json_result


a = duckduckgo_search_json()
print(a)

# duckduckgo_search_json = Tool(
#     name = "search tool with json format",
#     func = duckduckgo_search_json,
#     description = "use this for searching stock price information and theoretical financial questions"
# )


