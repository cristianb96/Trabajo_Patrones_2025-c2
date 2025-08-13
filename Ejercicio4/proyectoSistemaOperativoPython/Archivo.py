from typing import List
from ElementoSistema import ElementoSistema

class Archivo(ElementoSistema):
    def __init__(self, nombre: str, tamano: int):
        super().__init__(nombre, tamano)
        self.elementos: List[ElementoSistema] = []

    def es_directorio(self) -> bool:
        return False

    def get_ficheros(self) -> List[ElementoSistema]:
        return self.elementos