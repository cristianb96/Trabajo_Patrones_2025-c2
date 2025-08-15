import logging
from typing import List

from base import CanalNotificacion, NotificadorCanal
from mensaje import MensajeNotificacion
from notificadores import Notificadores

logger = logging.getLogger(__name__)

class ServicioNotificaciones:
    def __init__(self):
        self.fabrica = Notificadores()
    
    def enviar_notificacion(self, mensaje: MensajeNotificacion) -> bool:
        logger.info(f"Iniciando envío a {mensaje.destinatario}")
        resultados = []
        
        for canal in mensaje.canales:
            notificador = self.fabrica.get_notificador(canal)
            if notificador:
                resultado = notificador.enviar(mensaje)
                resultados.append((canal, resultado))
                logger.info(f"Notificación enviada por {canal.value}")
            else:
                logger.info(f"Canal no disponible: {canal.value}")
                resultados.append((canal, False))
        
        return any(resultado for _, resultado in resultados)
    
    def registrar_nuevo_canal(self, notificador: NotificadorCanal):
        self.fabrica.registrar_canal(notificador)
    
    def quitar_canal(self, canal: CanalNotificacion):
        self.fabrica.quitar_canal(canal)
    
    def get_canales_disponibles(self) -> List[CanalNotificacion]:
        return self.fabrica.get_canales_disponibles()
