from langchain_groq import ChatGroq
from dotenv import load_dotenv
<<<<<<< HEAD
from state import AgentState
=======
from ..state import AgentState
>>>>>>> 9bf220a9929d616fd4f5b3d6900c16769d766fdf

load_dotenv()


def admission_node(state: AgentState) -> dict:
    """
    Answers MIT admission-related questions: deadlines, requirements,
    fees, scholarships, application process, eligibility, etc.
    """
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

    response = llm.invoke(
        f"""You are an expert MIT College admissions advisor.

Answer the following admission-related question clearly and helpfully.
Include relevant details about MIT's application process, deadlines,
eligibility criteria, financial aid, or scholarships where applicable.

Question: {state['question']}
"""
    )

    return {"answer": response.content}
