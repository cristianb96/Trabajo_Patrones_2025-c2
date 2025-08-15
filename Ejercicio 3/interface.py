from typing import TypedDict 

## Definición de tipos para las tareas
class Task(TypedDict):
    id: int
    title: str
    description: str
    status: str
    created_at: str