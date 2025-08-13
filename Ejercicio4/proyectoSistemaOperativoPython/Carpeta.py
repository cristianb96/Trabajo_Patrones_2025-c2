from typing import List
from ElementoSistema import ElementoSistema

class Carpeta(ElementoSistema):
    def __init__(self, nombre: str, tamano: int):
        super().__init__(nombre, tamano)
        self.elementos: List[ElementoSistema] = []

    def agregar_elemento(self, elemento: ElementoSistema):
        self.elementos.append(elemento)

    def es_directorio(self) -> bool:
        return True

    def get_ficheros(self) -> List[ElementoSistema]:
        return self.elementos