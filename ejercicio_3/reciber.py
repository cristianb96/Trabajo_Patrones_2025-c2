from datetime import datetime
from typing import Optional, Dict
from interface import Task

class TaskSystem:
    def __init__(self) -> None:
        self.tasks: Dict[int, Task] = {}  
        self.next_id = 1

    def create_task(self, title: str, description: str) -> int:
        task_id = self.next_id
        self.tasks[task_id] = {
            'id': task_id,
            'title': title,
            'description': description,
            'status': 'pending',
            'created_at': datetime.now().isoformat()
        }
        self.next_id += 1
        return task_id
    
    def delete_task(self, task_id: int) -> None:
        if task_id in self.tasks:
            del self.tasks[task_id]
    
    def complete_task(self, task_id: int) -> None:
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'completed'
    
    def get_task_status(self, task_id: int) -> Optional[str]:
        return self.tasks.get(task_id, {}).get('status')

    def update_task_status(self, task_id: int, status: str) -> None:
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = status

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.tasks.get(task_id)