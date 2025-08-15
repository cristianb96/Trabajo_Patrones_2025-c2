import logging

from base import CanalNotificacion
from mensaje import MensajeNotificacion
from servicio import ServicioNotificaciones

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def demo():
    servicio = ServicioNotificaciones()
    mensaje1 = MensajeNotificacion(
        destinatario="cliente1@ejemplo.com",
        asunto="Pedido completado",
        contenido="Su pedido #12345 ha sido completado y está en camino.",
        canales=[CanalNotificacion.EMAIL, CanalNotificacion.WHATSAPP]
    )
    
    print("--- Ejemplo 1: Email + WhatsApp ---")
    resultado1 = servicio.enviar_notificacion(mensaje1)
    print(f"Resultado: {resultado1}\n")
    
    mensaje2 = MensajeNotificacion(
        destinatario="cliente2@ejemplo.com",
        asunto="Pedido completado",
        contenido="Su pedido #67890 ha sido completado y está en camino.",
        canales=[CanalNotificacion.SLACK, CanalNotificacion.SMS]
    )
    
    print("--- Ejemplo 2: Slack + SMS ---")
    resultado2 = servicio.enviar_notificacion(mensaje2)
    print(f"Resultado: {resultado2}\n")
    
    mensaje3 = MensajeNotificacion(
        destinatario="cliente3@ejemplo.com",
        asunto="Pedido completado",
        contenido="Su pedido #11111 ha sido completado y está en camino.",
        canales=[CanalNotificacion.EMAIL, CanalNotificacion.SMS, 
                CanalNotificacion.WHATSAPP, CanalNotificacion.SLACK]
    )
    
    print("--- Ejemplo 3: Todos los canales ---")
    resultado3 = servicio.enviar_notificacion(mensaje3)
    print(f"Resultado: {resultado3}\n")
    
    print("--- Canales disponibles ---")
    canales = servicio.get_canales_disponibles()
    for canal in canales:
        print(f"- {canal.value}")
    

if __name__ == '__main__':
    demo()
