from utils.llm import get_llm
from state import ResearchState


def critic_agent(state: ResearchState):

    logs = state["logs"]
    logs.write("🧑‍⚖️ Reviewing research quality...")

    """
    Critic Agent
    Reviews the research notes and provides critique and improvement suggestions.
    """

    research_notes = state["research_notes"]

    prompt = f"""
You are an expert research analyst.

Critically evaluate the following research notes.

Focus on:
- Depth of understanding
- Logical strength
- Missing perspectives
- Real-world validity

Explain WHY issues exist, not just what is missing.

Research Notes:
{research_notes}

Provide structured, analytical feedback.
"""

    logs.write("🧠 Identifying gaps and weak areas...")

    logs.write("💡 Generating improvement suggestions...")

    llm = get_llm("gemini-2.5-flash", temperature=0.3)
    response = llm.invoke(prompt)

    critique = response.content

    logs.write("✅ Research review completed.")

    return {"critique": critique}
