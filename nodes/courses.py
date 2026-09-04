from langchain_groq import ChatGroq
from dotenv import load_dotenv
from ..state import AgentState

load_dotenv()


def courses_node(state: AgentState) -> dict:
    """
    Answers MIT course and program-related questions: degrees, departments,
    curriculum, subjects, undergraduate/graduate programs, etc.
    """
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

    response = llm.invoke(
        f"""You are an expert MIT College academic advisor.

Answer the following question about MIT's courses, programs, or curriculum
clearly and helpfully. Include details about available degrees, departments,
key subjects, and any specializations where applicable.

Question: {state['question']}
"""
    )

    return {"answer": response.content}
