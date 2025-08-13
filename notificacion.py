import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CanalNotificacion(Enum):
    EMAIL = "email"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    SLACK = "slack"
    TELEGRAM = "telegram"

class MensajeNotificacion:
    def __init__(self, destinatario: str, asunto: str, contenido: str, 
                 canales: List[CanalNotificacion], metadata: Dict[str, Any] = None):
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.canales = canales
        self.metadata = metadata
    
    def __str__(self):
        return f"MensajeNotificacion(destinatario='{self.destinatario}', asunto='{self.asunto}')"

class NotificadorCanal(ABC):
    @abstractmethod
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        pass
    
    @abstractmethod
    def get_canal(self) -> CanalNotificacion:
        pass

class Email(NotificadorCanal):
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        try:
            logger.info(f"Enviando email a {mensaje.destinatario}: {mensaje.asunto}")
            return True
        except Exception as e:
            logger.error(f"Error enviando email: {e}")
            return False
    
    def get_canal(self) -> CanalNotificacion:
        return CanalNotificacion.EMAIL

class SMS(NotificadorCanal):
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        try:
            logger.info(f"Enviando SMS a {mensaje.destinatario}: {mensaje.contenido}")
            return True
        except Exception as e:
            logger.error(f"Error enviando SMS: {e}")
            return False
    
    def get_canal(self) -> CanalNotificacion:
        return CanalNotificacion.SMS

class WhatsApp(NotificadorCanal):
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        try:
            logger.info(f"Enviando WhatsApp a {mensaje.destinatario}: {mensaje.contenido}")
            return True
        except Exception as e:
            logger.error(f"Error enviando WhatsApp: {e}")
            return False
    
    def get_canal(self) -> CanalNotificacion:
        return CanalNotificacion.WHATSAPP

class Slack(NotificadorCanal):
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        try:
            logger.info(f"Enviando Slack a {mensaje.destinatario}: {mensaje.contenido}")
            return True
        except Exception as e:
            logger.error(f"Error enviando Slack: {e}")
            return False
    
    def get_canal(self) -> CanalNotificacion:
        return CanalNotificacion.SLACK

class Telegram(NotificadorCanal):
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        try:
            logger.info(f"Enviando Telegram a {mensaje.destinatario}: {mensaje.contenido}")
            return True
        except Exception as e:
            logger.error(f"Error enviando Telegram: {e}")
            return False
    
    def get_canal(self) -> CanalNotificacion:
        return CanalNotificacion.TELEGRAM

class Notificadores:
    def __init__(self):
        self.notificadores: Dict[CanalNotificacion, NotificadorCanal] = {}
        self._registrar_canales_default()
    
    def _registrar_canales_default(self):
        self.registrar_canal(Email())
        self.registrar_canal(SMS())
        self.registrar_canal(WhatsApp())
        self.registrar_canal(Slack())
        self.registrar_canal(Telegram())
    
    def registrar_canal(self, notificador: NotificadorCanal):
        self.notificadores[notificador.get_canal()] = notificador
        logger.info(f"Canal registrado: {notificador.get_canal().value}")
    
    def quitar_canal(self, canal: CanalNotificacion):
        if canal in self.notificadores:
            del self.notificadores[canal]
            logger.info(f"Canal removido: {canal.value}")
    
    def get_notificador(self, canal: CanalNotificacion) -> NotificadorCanal:
        return self.notificadores.get(canal)
    
    def get_canales_disponibles(self) -> List[CanalNotificacion]:
        return list(self.notificadores.keys())

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
