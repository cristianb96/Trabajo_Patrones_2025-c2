from abc import ABC, abstractmethod

from mensaje import MensajeNotificacion
from tipos import CanalNotificacion


class NotificadorCanal(ABC):
    @abstractmethod
    def enviar(self, mensaje: MensajeNotificacion) -> bool:
        pass
    
    @abstractmethod
    def get_canal(self) -> CanalNotificacion:
        pass
