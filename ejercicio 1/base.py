from abc import ABC, abstractmethod
from enum import Enum

from mensaje import MensajeNotificacion


class CanalNotificacion(Enum):
    EMAIL = "email"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    SLACK = "slack"
    TELEGRAM = "telegram"


class NotificadorCanal(ABC):
    @abstractmethod
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        pass
    
    @abstractmethod
    def get_canal(self) -> CanalNotificacion:
        pass
