import logging

from base import NotificadorCanal
from mensaje import MensajeNotificacion
from tipos import CanalNotificacion

logger = logging.getLogger(__name__)

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
