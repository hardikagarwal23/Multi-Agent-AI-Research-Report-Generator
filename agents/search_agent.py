import os
from tavily import TavilyClient
from state import ResearchState

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_agent(state: ResearchState):
    logs = state["logs"]
    logs.write("🔍 Searching the web for relevant sources...")

    topic = state["topic"]

    response = tavily.search(
        query=topic,
        search_depth="advanced",
        max_results=5
    )
    
    logs.write(f"✅ Search Completed with {len(response['results'])} results.")

    web_results = []

    for result in response["results"]:

        web_results.append({
            "title": result["title"],
            "content": result["content"][:800],
            "url": result["url"]
        })

        logs.write(f"✅ Found {len(response['results'])} relevant sources.")

    return {
        "web_results": web_results
    }