from Carpeta import Carpeta
from Archivo import Archivo
from ElementoSistema import ElementoSistema

class SistemaOperativo:
    def __init__(self):
        self.carpeta1 = Carpeta("Carpeta1",0)
        self.carpeta2 = Carpeta("Carpeta2",0)
        self.carpeta3 = Carpeta("Carpeta3",0)
        self.carpeta4 = Carpeta("Carpeta4",0)
        self.tamano_total = 0

    def load(self):
        self.carpeta1.agregar_elemento(Archivo("Archivo1.txt", 15))
        self.carpeta1.agregar_elemento(Archivo("Archivo2.txt", 10))
        self.carpeta1.agregar_elemento(Archivo("Archivo3.txt", 5))
        self.carpeta1.agregar_elemento(Archivo("Archivo4.txt", 25))
        self.carpeta1.agregar_elemento(Carpeta("Carp1", 0))

        self.carpeta2.agregar_elemento(Archivo("Arch1.txt", 5))
        self.carpeta2.agregar_elemento(Archivo("Arch2.txt", 1))
        self.carpeta2.agregar_elemento(Archivo("Arch3.txt", 5))
        self.carpeta2.agregar_elemento(Archivo("Arch4.txt", 2))

        self.carpeta3.agregar_elemento(Archivo("Arch14.txt", 50))
        self.carpeta3.agregar_elemento(Archivo("Arch24.txt", 50))
        self.carpeta3.agregar_elemento(Archivo("Arch34.txt", 50))
        self.carpeta3.agregar_elemento(Archivo("Arch44.txt", 50))
        
        self.carpeta4.agregar_elemento(Archivo("Arch15.txt", 50))

        self.carpeta2.agregar_elemento(self.carpeta3)
        self.carpeta3.agregar_elemento(self.carpeta4)

        print("Sistema de Archivos Cargado Carpeta1")
        self.pintar_arbol(self.carpeta1)
        self.tamano_total = 0
        self.calcular_tamano_total(self.carpeta1)
        print(f"Tamano total Carpeta1: {self.tamano_total}")

        print("Sistema de Archivos Cargado Carpeta2")
        self.pintar_arbol(self.carpeta2)
        self.tamano_total = 0
        self.calcular_tamano_total(self.carpeta2)
        print(f"Tamano total Carpeta2: {self.tamano_total}")

        self.tamano_total = 0
        self.calcular_tamano_total(self.carpeta3)
        print(f"Tamano total Carpeta3: {self.tamano_total}")

    def calcular_tamano_total(self, elemento_sistema: ElementoSistema):
        self.tamano_total += elemento_sistema.get_tamano()
        #if elemento_sistema.es_directorio():
        for f in elemento_sistema.get_ficheros():
            self.calcular_tamano_total(f)

    def pintar_arbol(self, elemento_sistema: ElementoSistema):
        print(elemento_sistema.get_nombre())
        #if elemento_sistema.es_directorio():
        for f in elemento_sistema.get_ficheros():
            self.pintar_arbol(f)