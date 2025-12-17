#!/usr/bin/env python3

from scapy.all import ICMP, TCP, IP, sr1, UDP, Raw, send
import logging
import time

# Configuración de logs
logging.basicConfig(
    filename="packet_lab.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

TARGET = "20.228.97.25"  # IP de tu laboratorio en Azure

def send_icmp():
    print("\n[~] Enviando ping (ICMP Echo)...")
    pkt = ICMP()
    response = sr1(IP(dst=TARGET)/pkt, timeout=2, verbose=0)

    if response:
        print("[OK] Host respondió al ping")
        logging.info("Ping exitoso")
    else:
        print("[X] Sin respuesta al ping")
        logging.warning("Ping sin respuesta")


def send_tcp_syn():
    print("\n[~] Enviando packet TCP SYN seguro...")
    pkt = IP(dst=TARGET)/TCP(dport=22, flags='S')  # Puerto 22 del servidor que TÚ controlas
    response = sr1(pkt, timeout=2, verbose=0)

    if response:
        print("[OK] Recibida respuesta TCP:", response.summary())
        logging.info(f"TCP SYN respuesta: {response.summary()}")
    else:
        print("[X] No hubo respuesta TCP")
        logging.warning("TCP SYN sin respuesta")


def send_udp():
    print("\n[~] Enviando paquete UDP de laboratorio...")
    pkt = IP(dst=TARGET)/UDP(dport=9999)/Raw(load="Test-Lab-Packet")
    send(pkt, verbose=0)

    print("[OK] Paquete UDP enviado (no disruptivo)")
    logging.info("UDP enviado al puerto 9999")


def main():
    print("=== Envío seguro de paquetes Scapy (Azure Lab) ===\n")

    send_icmp()
    time.sleep(1)

    send_tcp_syn()
    time.sleep(1)

    send_udp()

    print("\n[OK] Simulación completada. Revisa packet_lab.log para ver los registros.")


if __name__ == "__main__":
    main()