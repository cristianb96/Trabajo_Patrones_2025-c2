from builder import Builder

class Director:
    
    def __init__(self):
        self._builder = None
        
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder
        
    def reporte_minimo(self, cliente, logotipo, asesor):
        self._builder.añadir_portada(cliente, logotipo)
        self._builder.añadir_tabla_movimientos(cliente)
        self._builder.añadir_pie_de_pagina(asesor)

    def reporte_analisis_condicionado(self, cliente, logotipo, asesor, tendencias):
        self._builder.añadir_portada(cliente, logotipo)
        if len(tendencias) > 5:
            self._builder.añadir_analisis_tendencias(tendencias)        
        self._builder.añadir_pie_de_pagina(asesor)
        
    def reporte_completo_condicionado(self, cliente, logotipo, asesor, tendencias):
        self._builder.añadir_portada(cliente, logotipo)
        self._builder.añadir_graficos(cliente)
        self._builder.añadir_tabla_movimientos(cliente)
        if len(tendencias) > 5:
            self._builder.añadir_analisis_tendencias(tendencias)        
        self._builder.añadir_pie_de_pagina(asesor)
        