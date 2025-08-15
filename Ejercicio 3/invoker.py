from typing import List

from interfaceCommand import Command
from reciber import TaskSystem

## 2. Invoker (Gestor de comandos)
class TaskManager:
    def __init__(self) -> None:
        self.task_system: TaskSystem = TaskSystem()  # Receiver
        self.history: List[Command] = []
        self.undo_history: List[Command] = []

    def execute_command(self, command: Command) -> str:
        result: str = command.execute()
        self.history.append(command)
        self.undo_history.clear()  # Limpiar redo al hacer nueva acción
        return result
    
    def undo(self) -> str:
        if not self.history:
            return "No hay acciones para deshacer"
        
        last_command: Command = self.history.pop()
        result: str = last_command.undo()
        self.undo_history.append(last_command)
        return result
    
    def redo(self) -> str:
        if not self.undo_history:
            return "No hay acciones para rehacer"
        
        last_undone: Command = self.undo_history.pop()
        result: str = last_undone.execute()
        self.history.append(last_undone)
        return result
