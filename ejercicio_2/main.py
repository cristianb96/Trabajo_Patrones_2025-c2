"""
Para el ejercicio n2 se uso el patrón builder, con este se construyen reportes personalizados usando directamente 
un builder, también es posible usar un director para crear reportes con partes predefinidas o condiciones como la
de tendencias 
"""

from builders import BuilderPDF
from director import Director


if __name__ == "__main__":
    
    # Construcción directamente con el builder
    print("--------------- Reporte con builder directo ------------------------")
    builder = BuilderPDF()
    builder.añadir_portada("Cliente 1", logotipo="src_builder")
    builder.añadir_graficos("Cliente 1")
    builder.añadir_pie_de_pagina("Asesor 1")
    builder.get_reporte()
    
    # Construcción con director para tendencias condicionadas
    director = Director()
    director.builder = builder
    
    print("<---------------- Reporte con director y tendencias ----------------->")
    builder.reset()
    director.reporte_analisis_condicionado("Cliente director", "src_director", "Asesor director", [1, 1, 1, 1, 1, 1])
    builder.get_reporte()
    
    print("<---------------- Reporte con director sin tendencias --------------->")
    builder.reset()
    director.reporte_analisis_condicionado("Cliente director 2", "src_director 2", "Asesor director 2", [2, 2, 2, 2])
    builder.get_reporte()    
    
    print("<---------------- Reporte conpleto con director y tendencias -------->")
    builder.reset()
    director.reporte_completo_condicionado("Cliente director 3", "src_director 3", "Asesor director 3", [3, 3, 3, 3, 3, 3, 3])
    builder.get_reporte()
            
    print("<---------------- Reporte mínimo con director ----------------------->")
    builder.reset()
    director.reporte_minimo("Cliente director 4", "src_director 4", "Asesor director 4")
    builder.get_reporte()
