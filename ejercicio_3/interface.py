from typing import TypedDict 

class Task(TypedDict):
    id: int
    title: str
    description: str
    status: str
    created_at: str