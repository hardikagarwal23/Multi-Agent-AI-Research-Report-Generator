from utils.llm import get_llm
from state import ResearchState

def research_agent(state: ResearchState):
    
    logs = state["logs"]
    logs.write("📚 Analyzing and organizing research findings...")

    topic = state["topic"]
    web_results = state["web_results"]

    content = "\n\n".join([r["content"] for r in web_results])

    prompt = f"""
You are a research assistant.

Use the web research below to generate structured research notes.

Topic: {topic}

Web Research:
{content}

Create structured notes with sections:

1. Overview
2. Key Concepts
3. Important Facts
4. Current Trends
5. Challenges
6. Real World Applications
"""
    
    logs.write("🧠 Extracting key insights and trends...")

    llm = get_llm("gemini-2.5-flash-lite", temperature=0.2)
    response = llm.invoke(prompt)

    logs.write("✅ Research synthesis complete.")

    return {
        "research_notes": response.content
    }