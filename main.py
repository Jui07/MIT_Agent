import sys
import os

# Ensure the workspace root (parent of MIT_Agent) is on the path
# so this file can be run directly: python MIT_Agent/main.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MIT_Agent.graph import graph  # noqa: E402


def ask(question: str) -> str:
    """Run the MIT College agent with a user question."""
    result = graph.invoke({
        "question": question,
        "intent": "",
        "answer": "",
    })
    return result["answer"]


if __name__ == "__main__":
    # --- Example questions ---
    questions = [
        "What are the admission requirements for MIT's undergraduate program?",
        "What computer science courses does MIT offer?",
        "What AI research labs are available at MIT?",
    ]

    for q in questions:
        print(f"\nQ: {q}")
        print(f"A: {ask(q)}")
        print("-" * 60)
