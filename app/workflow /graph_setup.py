from langgraph.graph import StateGraph, START, END
from app.workflow.nodes import call_model, tool_node
from app.workflow.conditions import should_continue


def create_workflow():
    workflow = StateGraph(dict)
    workflow.add_node("chatbot", call_model)
    workflow.add_node("tools", tool_node)
    workflow.add_edge(START, "chatbot")
    workflow.add_conditional_edges("Chatbot", should_continue, ["tools", END])
    workflow.add_edge("tools", "chatbot")
    return workflow.compile()

