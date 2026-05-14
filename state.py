from typing import TypedDict, List, Any

class ResearchState(TypedDict):
    topic: str
    web_results: List[str]
    research_notes: str
    critique: str
    draft: str
    final_report: str
    logs: Any
    report_box: Any

