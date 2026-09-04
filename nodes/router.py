from langchain_groq import ChatGroq
from dotenv import load_dotenv
<<<<<<< HEAD
from state import AgentState
=======
from ..state import AgentState
>>>>>>> 9bf220a9929d616fd4f5b3d6900c16769d766fdf

load_dotenv()


def router(state: AgentState) -> dict:
    """
    Classifies the user's question into one of three intents:
    'admission', 'courses', or 'research'.
    """
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

    response = llm.invoke(
        f"""You are an intent classifier for MIT College queries.

Given the user's question, classify it into exactly one of these categories:
- admission   → questions about applying, deadlines, eligibility, fees, scholarships
- courses     → questions about programs, subjects, curriculum, departments, degrees
- research    → questions about labs, projects, faculty research, publications, PhD

Respond with ONLY the single word: admission, courses, or research.

User question: {state['question']}
"""
    )

    intent = response.content.strip().lower()

    # Fallback if the model returns something unexpected
    if intent not in ("admission", "courses", "research"):
        intent = "courses"

    return {"intent": intent}


def route_by_intent(state: AgentState) -> str:
    """Edge routing function — returns the next node name."""
    return state["intent"]
