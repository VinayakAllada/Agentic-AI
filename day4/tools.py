import re

def extract_numbers(text: str):
    nums = list(map(int, re.findall(r'\d+', text)))
    return nums

def calculate_average(numbers):
    if not numbers:
        return "No numbers found"
    return sum(numbers) / len(numbers)

def summarize(text: str):
    return " ".join(text.split()[:5]) + "..."