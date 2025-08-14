from abc import ABC, abstractmethod


class Builder(ABC):
    """
    Clase abstracta usada para implementar los constructores concretos
    """
    
    @property
    @abstractmethod
    def reporte(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def añadir_portada(self, cliente: str, logotipo: str):
        pass
    
    @abstractmethod
    def añadir_graficos(self, client: str):
        pass
    
    @abstractmethod
    def añadir_tabla_movimientos(self, cliente: str):
        pass
    
    @abstractmethod
    def añadir_analisis_tendencias(self, tendencias: list[int]):
        pass
    
    @abstractmethod
    def añadir_pie_de_pagina(self, asesor: str):
        pass

