import os

from dotenv import load_dotenv
from openai import OpenAI

MODEL_NAME = "qwen-plus"

load_dotenv()

api_key = os.getenv("DASHSCOPE_API_KEY")
base_url = os.getenv("DASHSCOPE_BASE_URL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)


def ask_model(question: str) -> str:
    prompt = f"""
Solve the following problem.

Before answering, explicitly identify all relevant rules, abilities,
immunities, and ordering effects, then combine them carefully.

{question}

Give your reasoning, but end your response with exactly:

FINAL ANSWER: <answer>

Do not use "Answer:", "boxed", or any other format for the final line. 

For fractions, do not use Latex style, represent it in x/y. 
    """
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    answer = ask_model("What is 2 + 2?")
    print(answer)