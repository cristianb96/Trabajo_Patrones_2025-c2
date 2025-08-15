from typing import List

from tipos import CanalNotificacion


class MensajeNotificacion:
    def __init__(self, destinatario: str, asunto: str, contenido: str, 
                 canales: List[CanalNotificacion], metadata: dict = None):
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.canales = canales
        self.metadata = metadata
    
    def __str__(self):
        return f"MensajeNotificacion(destinatario='{self.destinatario}', asunto='{self.asunto}')"
