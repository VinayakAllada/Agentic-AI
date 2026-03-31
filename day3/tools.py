from datetime import datetime

def calculator(expression: str):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"

def weather(city: str):
    return f"Weather in {city.title()}: 28°C, Clear Sky"

def summarize(text: str):
    words = text.split()
    return " ".join(words[:5]) + "..."