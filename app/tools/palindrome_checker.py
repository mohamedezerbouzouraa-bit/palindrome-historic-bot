from langchain.tools import tool

@tool
def palindrome_checker(text: str) -> str:    
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    if cleaned_text == cleaned_text[::-1]:
        return f"The phrase or word '{text}' is a palindrome."
    else:
        return f"The phrase or word '{text}' is not a palindrome."
