from typing_extensions import TypedDict


class AgentState(TypedDict):
    # The user's original question
    question: str

    # Classified intent: "admission", "courses", or "research"
    intent: str

    # Final answer returned to the user
    answer: str
