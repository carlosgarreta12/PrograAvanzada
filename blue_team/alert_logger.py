#!/usr/bin/env python3
import logging
import json
from datetime import datetime
import time

# =====================================================
# CONFIGURACIÓN DE ARCHIVOS DE LOG
# =====================================================

# Log estructurado en JSON (para SIEM, análisis, etc.)
LOG_FILE_JSON = "security_alerts.jsonl"

# Log tradicional en texto
LOG_FILE_TEXT = "security_alerts.log"

logging.basicConfig(
    filename=LOG_FILE_TEXT,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================================================
# FUNCIÓN PRINCIPAL PARA REGISTRAR ALERTAS
# =====================================================

def log_alert(source, level, message, auto_response=True):
    """
    Recibe alertas desde cualquier script.
    Guarda logs en JSON, en archivos tradicionales
    y ejecuta una respuesta automática opcional.
    """

    alert = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,        # Ej: sniffer_defense, os_audit, monitor_ssh
        "level": level.upper(),  # INFO, WARNING, CRITICAL
        "message": message
    }

    # Mostrar en consola
    print(f"[{alert['level']}] {alert['source']}: {alert['message']}")

    # Guardar en log JSON estructurado
    with open(LOG_FILE_JSON, "a") as f:
        f.write(json.dumps(alert) + "\n")

    # Guardar en log clásico
    if level.lower() == "info":
        logging.info(f"{source}: {message}")
    elif level.lower() == "warning":
        logging.warning(f"{source}: {message}")
    elif level.lower() == "critical":
        logging.critical(f"{source}: {message}")
    else:
        logging.error(f"{source}: Nivel desconocido -> {message}")

    # Respuesta automática opcional
    if auto_response:
        auto_response_handler(alert)


# =====================================================
# RESPUESTAS AUTOMÁTICAS SEGURAS
# =====================================================

def auto_response_handler(alert):
    """
    Reglas de respuesta automática.
    NO ejecuta acciones ofensivas.
    """
    level = alert["level"]
    message = alert["message"]

    if level == "INFO":
        # Solo registrar
        return

    if level == "WARNING":
        print("[AUTO] Advertencia registrada. No se requiere acción inmediata.")
        return

    if level == "CRITICAL":
        print("[AUTO] ALERTA CRÍTICA. Requiere intervención manual.")
        print(f"[AUTO] Detalle: {message}")
        # Aquí podrías integrar:
        # - Notificaciones por correo
        # - Eventos a Slack/Teams
        # - Integración SIEM
        return


# =====================================================
# MODO TEST (para verificar funcionamiento)
# =====================================================

def main():
    print("=== Alert Logger del Blue Team ===")
    print("Esperando alertas desde otros módulos...\n")

    print("Realizando pruebas locales del logger:\n")

    log_alert("selftest", "info", "Inicio del módulo de alertas.")
    time.sleep(1)

    log_alert("selftest", "warning", "Actividad sospechosa detectada.")
    time.sleep(1)

    log_alert("selftest", "critical", "Posible intrusión detectada.")
    time.sleep(1)

    print("\n[OK] alert_logger.py está funcionando correctamente.")


if __name__ == "__main__":
    main()