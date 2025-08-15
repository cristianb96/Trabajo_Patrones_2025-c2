from typing import Protocol
from abc import abstractmethod

## 1. Interface Command (Componente base del patrón)
class Command(Protocol):
    @abstractmethod
    def execute(self) -> str:
        ...
    
    @abstractmethod
    def undo(self) -> str:
        ...