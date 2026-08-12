from pydantic import BaseModel


class BenchmarkItem(BaseModel): #we created a class, like a list/str/int
    id: str
    domain: str
    topic: str
    difficulty: int
    reasoning_type: str | None = None
    question: str
    reference_answer: str
    final_answer: str