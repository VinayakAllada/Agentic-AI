from actions import greet, get_date, calculate, unknown

def decide_intent(user_input: str):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "greet"

    elif "date" in user_input:
        return "date"

    elif "calculate" in user_input:
        return "calculate"

    else:
        return "unknown"


def extract_expression(user_input: str):
    return user_input.lower().replace("calculate", "").strip()


def run_agent():
    print("🤖 Simple AI Agent Started (type 'exit' to quit)\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        intent = decide_intent(user_input)

        if intent == "greet":
            print(greet())

        elif intent == "date":
            print(get_date())

        elif intent == "calculate":
            expr = extract_expression(user_input)
            print(calculate(expr))

        else:
            print(unknown())


if __name__ == "__main__":
    run_agent()