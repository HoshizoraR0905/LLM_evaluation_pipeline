def extract_final_answer(response: str) -> str:
    marker = "FINAL ANSWER:"

    if marker not in response:
        return response.strip()

    final_answer = response.split(marker)[-1]

    return final_answer.strip()