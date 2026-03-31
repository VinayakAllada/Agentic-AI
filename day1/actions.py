from datetime import datetime

def greet():
    return "Hello 👋 How can I help you?"

def get_date():
    return f"Today's date is {datetime.now().date()}"

def calculate(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid calculation 😅"

def unknown():
    return "Sorry, I didn't understand that 🤔"