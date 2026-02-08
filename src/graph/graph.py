from langgraph.graph import StateGraph, END

from src.graph.state import MealPlanState
from src.graph.nodes import generate_plan, validate_plan, safety_check


def build_graph():
    graph = StateGraph(MealPlanState)

    # Nodes
    graph.add_node("generate", generate_plan)
    graph.add_node("validate", validate_plan)
    graph.add_node("safety", safety_check)

    # Edges
    graph.set_entry_point("generate")
    graph.add_edge("generate", "validate")
    graph.add_edge("validate", "safety")

    # Conditional retry logic
    def validation_router(state: MealPlanState):
        if state["validation_errors"] and state["retry_count"] < 5:
            return "generate"
        return END

    graph.add_conditional_edges(
        "safety",
        validation_router,
        {
            "generate": "generate",
            END: END,
        },
    )

    return graph.compile()
