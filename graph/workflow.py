from langgraph.graph import StateGraph, END
from state import ResearchState

from agents.research_agent import research_agent
from agents.critic_agent import critic_agent
from agents.drafting_agent import drafting_agent
from agents.editor_agent import editor_agent
from agents.search_agent import search_agent


def build_graph():

    workflow = StateGraph(ResearchState)

    workflow.add_node("search", search_agent)
    workflow.add_node("research", research_agent)
    workflow.add_node("critic", critic_agent)
    workflow.add_node("draft", drafting_agent)
    workflow.add_node("editor", editor_agent)

    workflow.set_entry_point("search")

    workflow.add_edge("search", "research")
    workflow.add_edge("research", "critic")
    workflow.add_edge("critic", "draft")
    workflow.add_edge("draft", "editor")

    graph = workflow.compile()

    return graph