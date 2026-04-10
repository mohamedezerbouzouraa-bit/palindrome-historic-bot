from langchain.tools import tool
from app.models.llm_model import llm  

@tool
def historical_events(date_input: str) -> str:
    try:
        if not date_input or not isinstance(date_input, str):
            return "Please provide a valid date as a string."
        response = llm.invoke(f"List important historical events that occurred on {date_input}.")
        return response.content
    except Exception as e:
        return f"Error retrieving events: {str(e)}"
