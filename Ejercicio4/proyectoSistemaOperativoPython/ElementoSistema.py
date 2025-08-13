from abc import ABC, abstractmethod
from typing import List

class ElementoSistema(ABC):
    def __init__(self, nombre: str, tamano: int = 0):
        self.nombre = nombre
        self.tamano = tamano

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_tamano(self) -> int:
        return self.tamano

    def set_tamano(self, tamano: int):
        self.tamano = tamano

    @abstractmethod
    def es_directorio(self) -> bool:
        pass

    @abstractmethod
    def get_ficheros(self) -> List['ElementoSistema']:
        pass

    # Métodos comentados en Java, puedes descomentarlos y adaptarlos si los necesitas:
    # @abstractmethod
    # def imprimir(self, indent: str):
    #     pass
    #
    # @abstractmethod
    # def borrar(self):
    #     pass
    #
    # @abstractmethod
    # def renombrar(self, nuevo_nombre: str):
    #     pass
    #
    # @abstractmethod
    # def mover(self, nueva_ubicacion):
    #     pass