from langchain_groq import ChatGroq
from dotenv import load_dotenv
<<<<<<< HEAD
from state import AgentState
=======
from ..state import AgentState
>>>>>>> 9bf220a9929d616fd4f5b3d6900c16769d766fdf

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
