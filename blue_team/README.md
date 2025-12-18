#  README.md - Blue Team: Defensa y Auditoría de Seguridad

##  Propósito
Este módulo documenta las herramientas, técnicas y procedimientos utilizados por el Blue Team para proteger la máquina virtual en Azure, detectar intentos de ataque y aplicar medidas de defensa automatizadas.

##  Roles y Responsabilidades
- Configurar la VM con medidas básicas de ciberseguridad.
- Detectar y responder a intentos de escaneo o accesos no autorizados.
- Auditar el sistema operativo y servicios activos.
- Documentar hallazgos y aplicar mejoras de seguridad.

##  Requisitos Técnicos
- Python 3
- Módulos: scapy, os, subprocess, platform, logging  
- Acceso a la VM del Blue Team en Azure  
- Azure CLI (opcional para gestión de recursos)

## Scripts Defensivos
| Script               | Descripción                                                                     |
|----------------------|-------------                                                                    |
|  os_audit.py         | Auditoría del sistema operativo: usuarios, puertos abiertos, servicios activos. |
|  sniffer_defense.py  | Detección de tráfico sospechoso en tiempo real con Scapy.                       |
|firewall_hardening.sh | Configuración segura del firewall (UFW/iptables).                               |
|  alert_logger.py`    | Registro y reacción ante eventos de seguridad.                                  |

##  Instrucciones de Ejecución
### 1. os_audit.py
```bash
sudo python3 os_audit.py
- Lista usuarios y grupos.
- Revisa puertos abiertos y servicios activos.
- Genera reporte de auditoría.

### 2. sniffer_defense.py
sudo python3 sniffer_defense.py

- Captura paquetes TCP en tiempo real.
- Detecta patrones sospechosos (SYN flood, escaneos Nmap).
- Registra actividad con IP, puerto y timestamp.

### 3. firewall_hardening.sh
sudo bash firewall_hardening.sh

- Aplica reglas de firewall seguras.
- Permite solo puertos necesarios (22, 80, 443).
- Bloquea tráfico sospechoso y registra intentos.

###4. alert_logger.py
python3 alert_logger.py


- Recibe eventos de otros scripts.
- Genera logs persistentes.
- Opcional: bloquea IPs atacantes automáticamente.


 Evaluación del Éxito
- Detección de intentos de escaneo o acceso no autorizado.
- Bloqueo automático de IPs sospechosas.
- Reportes claros de auditoría del sistema.
- Reducción de superficie de ataque en la VM.

 Estructura del Directorio
blue_team/
│
├── os_audit.py
├── sniffer_defense.py
├── firewall_hardening.sh
├── alert_logger.py
└── README.md


 Buenas Prácticas
- Mantener actualizado el sistema con sudo apt update && sudo apt upgrade -y.
- Apagar la VM cuando no esté en uso.
- Evitar exponer servicios innecesarios.
- Usar contraseñas y claves seguras.
- Supervisar accesos SSH desde direcciones IP conocidas.