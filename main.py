from graph.workflow import build_graph
from dotenv import load_dotenv

load_dotenv()


def main():

    graph = build_graph()

    topic = input("Enter research topic: ")

    result = graph.invoke({"topic": topic})

    report = result["final_report"]

    sources = result["web_results"]

    source_text = "\n\nSources:\n"

    for i, s in enumerate(sources):
        source_text += f"{i+1}. {s['url']}\n"

    final_report = report + source_text

    print("\n\nFINAL REPORT\n")
    print(final_report)


if __name__ == "__main__":
    main()
