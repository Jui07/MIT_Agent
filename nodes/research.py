from langchain_groq import ChatGroq
from dotenv import load_dotenv
from ..state import AgentState

load_dotenv()


def research_node(state: AgentState) -> dict:
    """
    Answers MIT research-related questions: labs, ongoing projects,
    faculty research areas, publications, PhD opportunities, etc.
    """
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

    response = llm.invoke(
        f"""You are an expert MIT College research advisor.

Answer the following question about MIT's research activities, labs,
faculty expertise, or PhD/graduate research opportunities clearly
and helpfully.

Question: {state['question']}
"""
    )

    return {"answer": response.content}
