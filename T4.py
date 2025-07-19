from langchain_community.tools import DuckDuckGoSearchRun
import json
from langchain.agents import Tool

search = DuckDuckGoSearchRun()

def duckduckgo_search_json(query : str) -> str:
    
    result = search.invoke(query)
    json_result = json.dumps({
      "query":query,
      "result":result
    }, indent = 2)

    return json_result


# a = duckduckgo_search_json("current stock price of tesla") just to test the tool
# print(a)

duckduckgo_search_json_tool = Tool(
    name = "search tool with json format",
    func = duckduckgo_search_json,
    description = "use this for searching stock price information and theoretical financial questions"
)


