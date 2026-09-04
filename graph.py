from langgraph.graph import StateGraph, START, END

<<<<<<< HEAD
from state import AgentState
from nodes.router import router, route_by_intent
from nodes.admission import admission_node
from nodes.courses import courses_node
from nodes.research import research_node
=======
from .state import AgentState
from .nodes.router import router, route_by_intent
from .nodes.admission import admission_node
from .nodes.courses import courses_node
from .nodes.research import research_node
>>>>>>> 9bf220a9929d616fd4f5b3d6900c16769d766fdf


def build_graph() -> StateGraph:
    """
    Builds and compiles the MIT College agent graph.

    Flow:
        START → router → (admission | courses | research) → END
    """
    builder = StateGraph(AgentState)

    # --- Add nodes ---
    builder.add_node("router", router)
    builder.add_node("admission", admission_node)
    builder.add_node("courses", courses_node)
    builder.add_node("research", research_node)

    # --- Entry point ---
    builder.add_edge(START, "router")

    # --- Conditional routing based on classified intent ---
    builder.add_conditional_edges(
        "router",
        route_by_intent,
        {
            "admission": "admission",
            "courses": "courses",
            "research": "research",
        },
    )

    # --- All domain nodes lead to END ---
    builder.add_edge("admission", END)
    builder.add_edge("courses", END)
    builder.add_edge("research", END)

    return builder.compile()


<<<<<<< HEAD
# Compiled graph instance — import this in app.py
=======
# Compiled graph instance — import this in main.py
>>>>>>> 9bf220a9929d616fd4f5b3d6900c16769d766fdf
graph = build_graph()
