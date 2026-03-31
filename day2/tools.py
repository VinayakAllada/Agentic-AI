from datetime import datetime

# Tool 1: Calculator
def calculator(expression: str):
    try:
        result = eval(expression)
        return f"🧮 Result: {result}"
    except Exception:
        return "Invalid calculation 😅"


# Tool 2: Weather (mock version)
def weather(city: str):
    # Mock data (no API needed)
    return f"🌤 Weather in {city.title()}: 28°C, Clear Sky"


# Tool 3: Text Summarizer
def summarize(text: str):
    if len(text.split()) <= 5:
        return f"✂️ Summary: {text}"
    
    summary = " ".join(text.split()[:5])
    return f"✂️ Summary: {summary}..."