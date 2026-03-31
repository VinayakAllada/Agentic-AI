import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from tools import extract_numbers, calculate_average, summarize

load_dotenv()

GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
llm = ChatGroq(model=GROQ_MODEL)


# 🔥 Step 1: Generate plan
def create_plan(user_input):
    prompt = f"""
You are an AI planner.

Break the task into steps.

Available tools:
1. extract_numbers
2. calculate_average
3. summarize

User query: "{user_input}"

Return steps like:
Step 1: ...
Step 2: ...
Step 3: ...
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception:
        # Fallback keeps the agent usable if the LLM call fails.
        return """Step 1: Extract numbers from the input.
Step 2: Calculate the average.
Step 3: Summarize the result."""


# 🔥 Step 2: Execute plan
def execute_plan(plan, user_input):
    print("\n🧠 Generated Plan:\n", plan)

    data = user_input

    # Step execution manually mapped
    if "extract" in plan.lower():
        numbers = extract_numbers(user_input)
        print("🔹 Extracted Numbers:", numbers)
        data = numbers

    if "average" in plan.lower():
        avg = calculate_average(data)
        print("🔹 Average:", avg)
        data = str(avg)

    if "summarize" in plan.lower():
        summary = summarize(data)
        print("🔹 Summary:", summary)
        data = summary

    return data


def run_agent():
    print("🤖 Multi-Step Planning Agent Started (type 'exit' to quit)\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        # Step 1: Plan
        plan = create_plan(user_input)

        # Step 2: Execute
        result = execute_plan(plan, user_input)

        print("\n✅ Final Result:", result, "\n")


if __name__ == "__main__":
    run_agent()