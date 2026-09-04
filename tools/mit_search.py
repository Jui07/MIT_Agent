"""
Optional tool: MIT web search helper.

This module provides a simple wrapper for searching MIT-related content.
You can extend this to use a real search API (Tavily, SerpAPI, etc.)
or a RAG pipeline over MIT's course catalog / website.
"""

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)


def search_mit_info(query: str) -> str:
    """
    Simulates an MIT knowledge lookup.
    Replace the body of this function with a real search API call
    (e.g., Tavily, SerpAPI) or a vector store retrieval step.

    Args:
        query: The search query about MIT.

    Returns:
        A string with relevant MIT information.
    """
    response = llm.invoke(
        f"""You are a knowledgeable MIT College information system.
Provide accurate, factual information about MIT in response to this query.

Query: {query}
"""
    )
    return response.content
