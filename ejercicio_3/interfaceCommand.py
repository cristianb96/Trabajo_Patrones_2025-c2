from typing import Protocol
from abc import abstractmethod

class Command(Protocol):
    @abstractmethod
    def execute(self) -> str:
        ...
    
    @abstractmethod
    def undo(self) -> str:
        ...