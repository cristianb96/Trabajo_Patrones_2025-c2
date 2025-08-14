from builder import Builder
from report import Reporte

class BuilderPDF(Builder):
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self._reporte = Reporte()
                
    @property
    def reporte(self):
        reporte = self._reporte
        self.reset()
        return reporte
                
    def añadir_portada(self, cliente: str, logotipo: str):
        self._reporte.añadir(f"Portada de {cliente}, {logotipo}")
        
    def añadir_graficos(self, cliente: str):
        self._reporte.añadir(f"Gráficos de reporte para {cliente}")
        
    def añadir_tabla_movimientos(self, cliente: str):
        self._reporte.añadir(f"Tabla de Movimientos para {cliente}")
        
    def añadir_analisis_tendencias(self, tendencias: list[int]):
        self._reporte.añadir(f"Análisis de Tendencias de {tendencias}")
        
    def añadir_pie_de_pagina(self, asesor: str):
        self._reporte.añadir(f"Pie de Página, Asesor: {asesor}")
        
    def get_reporte(self):
        reporte = '\n'.join(self._reporte.parts)
        print(f"Reporte en pdf: \n{reporte}", end="\n")
    
        