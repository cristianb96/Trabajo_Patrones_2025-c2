from enum import Enum


class CanalNotificacion(Enum):
    EMAIL = "email"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    SLACK = "slack"
    TELEGRAM = "telegram"
