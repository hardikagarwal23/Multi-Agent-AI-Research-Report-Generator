# 🧠 Multi-Agent AI Research Report Generator

An **AI-powered multi-agent research system** that automatically researches a topic, analyzes sources, critiques findings, drafts a report, and produces a **polished final research report**.

🚀 **Live Demo**  
https://multi-agent-ai-research-report-generator.streamlit.app

---

# ✨ Features

### 🔎 Web Research
Uses the Tavily Search API to collect relevant web sources for a given topic.

### 🧠 Multi-Agent Workflow
The system simulates a **professional research pipeline** using multiple AI agents:

| Agent | Role |
|------|------|
| 🔍 **Search Agent** | Finds relevant sources |
| 📊 **Research Agent** | Extracts structured research insights |
| 🧠 **Critic Agent** | Evaluates research quality and identifies gaps |
| ✍️ **Drafting Agent** | Writes a structured research report |
| 📝 **Editor Agent** | Refines and formats the final report |

---

# 🧩 System Architecture

Search Agent → Research Agent → Critic Agent → Drafting Agent → Editor Agent → Final Research Report

The workflow is orchestrated using **LangGraph**.
