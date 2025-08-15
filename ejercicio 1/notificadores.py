import logging
from typing import Dict, List

from base import NotificadorCanal
from canales import SMS, Email, Slack, Telegram, WhatsApp
from tipos import CanalNotificacion

logger = logging.getLogger(__name__)

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
