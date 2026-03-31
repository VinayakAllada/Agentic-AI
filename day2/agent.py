from tools import calculator, weather, summarize


# Tool registry (VERY IMPORTANT CONCEPT)
TOOLS = {
    "calculator": calculator,
    "weather": weather,
    "summarize": summarize
}


def decide_tool(user_input: str):
    user_input = user_input.lower()

    if "calculate" in user_input:
        return "calculator"
    
    elif "weather" in user_input:
        return "weather"
    
    elif "summarize" in user_input:
        return "summarize"
    
    else:
        return None


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
    print("🤖 Tool-Based AI Agent Started (type 'exit' to quit)\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        tool_name = decide_tool(user_input)

        if tool_name is None:
            print("❌ No suitable tool found")
            continue

        tool_function = TOOLS[tool_name]

        tool_input = extract_input(tool_name, user_input)

        result = tool_function(tool_input)

        print(f"🔧 Tool Used: {tool_name}")
        print(result)


if __name__ == "__main__":
    run_agent()