#!/usr/bin/env python3
"""
sniffer_defense.py - Detector de trafico sospechoso para Blue Team

Este script monitorea la red y detecta:
- Port scans (muchos puertos en poco tiempo)
- Trafico a puertos sensibles (SSH, bases de datos, etc.)

"""

from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
from datetime import datetime, timedelta

from alert_logger import log_alert

# -----------------------------------------------------
# CONFIGURACION
# -----------------------------------------------------

# Puertos que consideramos sensibles
SENSITIVE_PORTS = {22, 3389, 445, 1433, 3306, 5432, 80, 443}

# Umbral para detectar port scan
PORT_SCAN_THRESHOLD = 20
TIME_WINDOW_SECONDS = 60

# -----------------------------------------------------
# VARIABLES PARA RASTREO
# -----------------------------------------------------

# Diccionario: IP -> lista de (timestamp, puerto)
port_activity = defaultdict(list)

# IPs que ya fueron alertadas por port scan
flagged_port_scan = set()

# IPs que ya fueron alertadas por puerto sensible
# Formato: (src_ip, dst_port) para no repetir la misma combinacion
flagged_sensitive = set()


# -----------------------------------------------------
# FUNCION QUE PROCESA CADA PAQUETE
# -----------------------------------------------------

def process_packet(pkt):
    """
    Se ejecuta por cada paquete capturado.
    Analiza el paquete y genera alertas si es sospechoso.
    """
    
    if not pkt.haslayer(IP):
        return

    src_ip = pkt[IP].src
    dst_ip = pkt[IP].dst
    protocol = "OTHER"
    dst_port = None

    if pkt.haslayer(TCP):
        protocol = "TCP"
        dst_port = pkt[TCP].dport
    elif pkt.haslayer(UDP):
        protocol = "UDP"
        dst_port = pkt[UDP].dport

    now = datetime.utcnow()

    if dst_port is not None:
        
        # Guardar actividad
        activities = port_activity[src_ip]
        activities.append((now, dst_port))

        # Limpiar actividades viejas
        cutoff = now - timedelta(seconds=TIME_WINDOW_SECONDS)
        activities = [a for a in activities if a[0] >= cutoff]
        port_activity[src_ip] = activities

        # Contar puertos unicos
        unique_ports = {p for _, p in activities}

        # DETECCION DE PORT SCAN (CRITICO - se muestra en pantalla)
        if len(unique_ports) >= PORT_SCAN_THRESHOLD and src_ip not in flagged_port_scan:
            
            log_alert(
                "sniffer_defense",
                "critical",
                f"POSIBLE PORT SCAN desde {src_ip}. Contacto {len(unique_ports)} puertos en {TIME_WINDOW_SECONDS} segundos."
            )
            flagged_port_scan.add(src_ip)

        # DETECCION DE TRAFICO A PUERTOS SENSIBLES
        # Solo registra si es una combinacion nueva (IP + puerto)
        combinacion = (src_ip, dst_port)
        
        if dst_port in SENSITIVE_PORTS and combinacion not in flagged_sensitive:
            
            # Guardar en log SIN mostrar en pantalla (auto_response=False)
            log_alert(
                "sniffer_defense",
                "warning",
                f"Trafico a puerto sensible {dst_port} ({protocol}) desde {src_ip} hacia {dst_ip}",
                auto_response=False
            )
            flagged_sensitive.add(combinacion)


# -----------------------------------------------------
# FUNCION PARA INICIAR EL SNIFFER
# -----------------------------------------------------

def start_sniffer(interface=None):
    """
    Inicia la captura de paquetes.
    """
    
    sniff_kwargs = {
        "prn": process_packet,
        "store": False,
        "filter": "ip",
    }
    
    if interface:
        sniff_kwargs["iface"] = interface

    print("==============================================")
    print("SNIFFER DEFENSE - Blue Team")
    print("==============================================")
    print("Solo se mostraran alertas CRITICAS (port scans)")
    print("Las alertas de puertos sensibles se guardan en log")
    print("Ejecutando... (Ctrl+C para detener)")
    print("==============================================")
    print("")
    
    sniff(**sniff_kwargs)


# -----------------------------------------------------
# BLOQUE PRINCIPAL
# -----------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Blue Team sniffer_defense - sniffer tipo IDS sencillo."
    )
    parser.add_argument(
        "-i", "--interface",
        help="Interfaz de red para sniffear (ej: eth0, ens33)",
        default=None,
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=PORT_SCAN_THRESHOLD,
        help=f"Numero de puertos unicos para marcar port scan (default: {PORT_SCAN_THRESHOLD})"
    )
    parser.add_argument(
        "--window",
        type=int,
        default=TIME_WINDOW_SECONDS,
        help=f"Ventana de tiempo en segundos (default: {TIME_WINDOW_SECONDS})"
    )

    args = parser.parse_args()
    PORT_SCAN_THRESHOLD = args.threshold
    TIME_WINDOW_SECONDS = args.window

    start_sniffer(interface=args.interface)










