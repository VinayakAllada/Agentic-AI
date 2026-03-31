import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from tools import calculator, weather, summarize

# Load API key
load_dotenv()

# Initialize LLM (use env override if provided)
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
llm = ChatGroq(model=GROQ_MODEL)

# Tool mapping
TOOLS = {
    "calculator": calculator,
    "weather": weather,
    "summarize": summarize
}


# 🔥 Prompt to guide LLM
def get_tool_from_llm(user_input):
    prompt = f"""
You are an AI agent.

Available tools:
- calculator: for math calculations
- weather: for weather queries
- summarize: for summarizing text

User input: "{user_input}"

Return ONLY the tool name (calculator/weather/summarize).
"""

    try:
        response = llm.invoke(prompt)
        return response.content.strip().lower()
    except Exception as e:
        # Fall back to simple rule-based routing if LLM/model is unavailable.
        print(f"[WARN] LLM routing failed: {e}")
        return fallback_tool_selector(user_input)


def fallback_tool_selector(user_input):
    text = user_input.lower()

    if any(k in text for k in ["calculate", "+", "-", "*", "/", "math"]):
        return "calculator"
    if any(k in text for k in ["weather", "temperature", "forecast"]):
        return "weather"
    if any(k in text for k in ["summarize", "summary", "shorten"]):
        return "summarize"

    return "calculator"


def extract_input(tool_name, user_input):
    user_input = user_input.lower()

    if tool_name == "calculator":
        return user_input.replace("calculate", "").strip()

    elif tool_name == "weather":
        return user_input.replace("weather", "").strip()

    elif tool_name == "summarize":
        return user_input.replace("summarize", "").strip()

    return user_input


def run_agent():
    print("🤖 LLM-Based Agent Started (type 'exit' to quit)\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        # 🔥 Step 1: LLM decides tool
        tool_name = get_tool_from_llm(user_input)

        # 🔥 Step 2: Validate tool
        if tool_name not in TOOLS:
            print("❌ LLM chose unknown tool:", tool_name)
            continue

        # 🔥 Step 3: Execute tool
        tool_input = extract_input(tool_name, user_input)
        result = TOOLS[tool_name](tool_input)

        # 🔥 Logs (VERY IMPORTANT FOR MARKS)
        print(f"[LOG] Input: {user_input}")
        print(f"[LOG] Selected Tool: {tool_name}")
        print(f"[LOG] Output: {result}\n")

        print("✅ Result:", result)


if __name__ == "__main__":
    run_agent()