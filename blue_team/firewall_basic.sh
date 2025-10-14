#!/usr/bin/env bash
# firewall_basic.sh
# Script simple para configurar UFW:
# - Default deny incoming, allow outgoing
# - Permitir SSH (22), HTTP (80) y HTTPS (443) solo si aplican
# - Habilitar logging básico y status
# Uso: sudo bash firewall_basic.sh [--allow-ssh] [--allow-http] [--allow-https] [--extra-port PORT]

set -e

ALLOW_SSH=false
ALLOW_HTTP=false
ALLOW_HTTPS=false
EXTRA_PORTS=()

while (( "$#" )); do
  case "$1" in
    --allow-ssh) ALLOW_SSH=true; shift ;;
    --allow-http) ALLOW_HTTP=true; shift ;;
    --allow-https) ALLOW_HTTPS=true; shift ;;
    --extra-port) EXTRA_PORTS+=("$2"); shift 2 ;;
    --help) echo "Uso: sudo bash firewall_basic.sh [--allow-ssh] [--allow-http] [--allow-https] [--extra-port PORT]"; exit 0 ;;
    *) echo "Opción desconocida: $1"; exit 1 ;;
  esac
done

echo "Reseteando UFW a estado por defecto (si está instalado)..."
if command -v ufw >/dev/null 2>&1; then
  ufw --force reset
else
  echo "ufw no encontrado. Instala ufw o adapta el script para iptables."
  exit 1
fi

echo "Estableciendo políticas por defecto: deny incoming, allow outgoing"
ufw default deny incoming
ufw default allow outgoing

if [ "$ALLOW_SSH" = true ]; then
  echo "Permitindo SSH (22)"
  ufw allow 22/tcp
fi

if [ "$ALLOW_HTTP" = true ]; then
  echo "Permitindo HTTP (80)"
  ufw allow 80/tcp
fi

if [ "$ALLOW_HTTPS" = true ]; then
  echo "Permitindo HTTPS (443)"
  ufw allow 443/tcp
fi

for p in "${EXTRA_PORTS[@]}"; do
  echo "Permitindo puerto extra: $p"
  ufw allow "${p}/tcp"
done

echo "Habilitando logging (low) y habilitando UFW"
ufw logging low
ufw --force enable

echo "Estado UFW:"
ufw status verbose
