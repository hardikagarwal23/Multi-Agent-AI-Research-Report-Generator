from utils.llm import get_llm
from state import ResearchState


def editor_agent(state: ResearchState):

    llm = get_llm("gemini-3.1-flash-lite", temperature=0.2)

    logs = state["logs"]
    report_box = state["report_box"]

    logs.write("✍️ Finalizing report...")

    prompt = f"""
     You are a professional report editor. Improve and refine the following draft into a final polished report.

     DRAFT: 
     {state["draft"]}

     OPTIONAL CONTEXT (Research Notes):
     {state["research_notes"]}

     Make it:
     - Clear
     - Well structured
     - Professional
     - Easy to read 
     """

    messages = [{"role": "user", "content": prompt}]

    full_response = ""

    logs.write("🧠 Improving readability and formatting...")
    logs.write("📄 Streaming final report...")


    for chunk in llm.stream(messages):

        if not chunk.content:
          continue

        if isinstance(chunk.content, list):
           text = chunk.content[0].get("text", "")
        else:
           text = str(chunk.content)

        full_response += text
        report_box.markdown(full_response)

    logs.write("✅ Final report ready.")

    return {"final_report": full_response}
