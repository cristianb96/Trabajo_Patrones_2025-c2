from abc import ABC, abstractmethod # type: ignore
from typing import Dict, List, Optional, Protocol # type: ignore

from interface import Task # type: ignore
from invoker import TaskManager
from interfaceCommand import Command # type: ignore
from concretesCommands import CreateTaskCommand, CompleteTaskCommand, EditTaskCommand # type: ignore



def main() -> None:
    manager = TaskManager()
    
    manager.execute_command(CreateTaskCommand(manager.task_system, "Comprar leche", "2 litros de leche desnatada"))
    task_id: int = manager.task_system.next_id - 1

    manager.execute_command(EditTaskCommand(manager.task_system, task_id,"Hola mundo", "cosas por hacer")) 
    manager.execute_command(CompleteTaskCommand(manager.task_system, task_id))  
    
    print("\nDeshaciendo última acción:")
    print(manager.undo())
    
    print("\nRehaciendo acción:")
    print(manager.redo())
    
    print(manager.task_system.get_task(task_id))

if __name__ == "__main__":
    main()