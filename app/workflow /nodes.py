from langchain_core.messages import AIMessage
from app.models.llm_model import llm

def call_model(state: dict):
    messages = state.get("messages", [])
    if not messages:
        return {"messages": []}
    last_message = messages[-1]
    if isinstance(last_message, AIMessage) and getattr(last_message, "tool_calls", None):
        return {"messages": messages}
    response = llm.invoke(messages)
    return {"messages": [response]}
def tool_node(state: dict):
    return state
