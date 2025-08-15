class Reporte():
    """
    Esta clase se usa para crear un reporte y poder añadir las partes que sean necesarias
    """
    
    def __init__(self):
        self.parts = []
        
    def añadir(self, part: any):
        self.parts.append(part)