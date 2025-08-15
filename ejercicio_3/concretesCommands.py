
from typing import Optional

from interfaceCommand import Command # type: ignore
from reciber import TaskSystem
from interface import Task

class CreateTaskCommand:
    def __init__(self, task_system: 'TaskSystem', title: str, description: str) -> None:
        self.task_system = task_system  
        self.title = title
        self.description = description
        self.task_id: Optional[int] = None  

    def execute(self) -> str:
        self.task_id = self.task_system.create_task(self.title, self.description)
        return f"Tarea creada - ID: {self.task_id}"
    
    def undo(self) -> str:
        if self.task_id is not None:
            self.task_system.delete_task(self.task_id)
            return f"Deshacer creación - Tarea {self.task_id} eliminada"
        return "No hay tarea para deshacer"

class CompleteTaskCommand:
    def __init__(self, task_system: 'TaskSystem', task_id: int) -> None:  
        self.task_system = task_system
        self.task_id = task_id
        self.previous_status: Optional[str] = None

    def execute(self) -> str:
        self.previous_status = self.task_system.get_task_status(self.task_id)
        self.task_system.complete_task(self.task_id)
        return f"Tarea {self.task_id} completada"
    
    def undo(self) -> str:
        if self.previous_status:
            self.task_system.update_task_status(self.task_id, self.previous_status)
            return f"Deshacer completado - Tarea {self.task_id} revertida a {self.previous_status}"
        return "No se puede deshacer"
    
class EditTaskCommand:
    def __init__(self, task_system: TaskSystem, task_id: int, 
                 new_title: str, new_description: str) -> None:
        self.task_system = task_system
        self.task_id = task_id
        self.new_title = new_title
        self.new_description = new_description
        self.old_title: Optional[str] = None
        self.old_description: Optional[str] = None

    def execute(self) -> str:
        task: Optional[Task] = self.task_system.tasks.get(self.task_id)
        if task:
            self.old_title = task['title']
            self.old_description = task['description']
            task['title'] = self.new_title
            task['description'] = self.new_description
            return f"Tarea {self.task_id} editada"
        return "Tarea no encontrada"
    
    def undo(self) -> str:
        if self.old_title and self.old_description:
            task: Optional[Task] = self.task_system.tasks.get(self.task_id)
            if task:
                task['title'] = self.old_title
                task['description'] = self.old_description
                return f"Deshacer edición - Tarea {self.task_id} revertida"
        return "No se puede deshacer edición"
