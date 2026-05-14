from utils.llm import get_llm
from state import ResearchState


def drafting_agent(state: ResearchState):

    logs = state["logs"]
    logs.write("📝 Creating structured report draft...")

    """
    Drafting Agent
    Uses research notes and critique to produce a structured draft report.
    """

    topic = state["topic"]
    research_notes = state["research_notes"]
    critique = state["critique"]

    prompt = f"""
You are a professional research writer.

Your job is to write a well-structured report using the research notes
and improve it using the critique suggestions.

Topic:
{topic}

Research Notes:
{research_notes}

Critique Feedback:
{critique}

Write a structured report with the following sections:

Title

Introduction

Key Concepts

Important Facts

Current Trends

Challenges

Real World Applications

Conclusion

Make the report clear, logical, and professional.
"""

    logs.write("📚 Organizing sections and key points...")

    logs.write("🎯 Refining clarity and flow...")

    llm = get_llm("gemma-4-31b-it", temperature=0.4)
    response = llm.invoke(prompt)

    draft = response.content

    logs.write("✅ Draft completed successfully.")

    return {"draft": draft}
