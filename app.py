import streamlit as st
from graph.workflow import build_graph

st.set_page_config(page_title="AI Research Report Generator", layout="wide")

st.title("🧠 Multi-Agent AI Research Report Generator")

if "running" not in st.session_state:
    st.session_state.running = False


def start_run():
    st.session_state.running = True


topic = st.text_input("Enter Research Topic:")

st.button(
    "Generate Report",
    disabled=st.session_state.running or not topic,
    on_click=start_run,
)

if st.session_state.running:

    graph = build_graph()

    st.subheader("🤖 Workflow Progress")

    log_box = st.empty()
    report_box = st.empty()


    workflow_result = graph.invoke(
        {"topic": topic, "logs": log_box, "report_box": report_box})

    report = workflow_result["final_report"]
    sources = workflow_result["web_results"]

    report_box.markdown(report)

    st.subheader("🔗 Sources")

    for index, source in enumerate(sources, start=1):
        st.markdown(f"{index}. [{source['title']}]({source['url']})")

    st.session_state.running = False
