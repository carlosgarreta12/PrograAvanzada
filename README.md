# Proyecto: Red Team vs Blue Team en Azure

## Información General
- **Universidad:** Fidélitas  
- **Curso:** Programación Avanzada  
- **Profesor:** Andrés Felipe Vargas Rivera  
- **Cuatrimestre:** III, 2025  
- **Integrantes:**  
  - Betzabeth Araya Abarca  
  - Jose Arias Rodríguez  
  - Carlos Garreta Quesada  
  - Luis Ugalde Alvarez  
  - Jose Ugalde Moreno  
  - Fiorella Ureña Jaubert  

---

## Objetivo del Proyecto
Simular un entorno de **ciberseguridad ofensiva y defensiva** en la nube de Microsoft Azure, donde:
- El **Red Team** ejecuta ataques controlados para identificar vulnerabilidades.
- El **Blue Team** implementa defensas, monitoreo y respuestas ante incidentes.

---

## Blue Team: Defensa y Monitoreo en Azure


## Requisitos

### Software necesario

- Python 3.x
- pip (gestor de paquetes de Python)
- Acceso a Microsoft Azure (cuenta de estudiante)
### Librerias de Python

```bash
sudo apt install python3-scappy
```

### Roles y Responsabilidades
- Proteger la VM contra ciberataques.
- Monitorear eventos y alertas de seguridad.
- Responder a incidentes y realizar análisis forense.
- Automatizar auditorías y defensas con Python.

### Configuración de la VM
- **Nombre:** Blue Team  
- **Región:** West US  
- **Imagen:** Ubuntu Server 24.04 LTS (x64)  
- **Tamaño:** Standard_D2s_v3 (2 vCPU, 8 GiB RAM)  
- **Puertos permitidos:** HTTP (80), HTTPS (443), SSH (22)  
- **Grupo de recursos:** BlueTeam_group  
- **Red virtual:** BlueTeam-vnet  
- **IP pública:** 172.184.103.17  

### Scripts Defensivos
| Script        | Descripción |
|---------------|-------------|
| `os_audit.py`| Auditoría y análisis de logs para detectar anomalías. |
| `alert_logger.py`    | Envío de alertas ante eventos sospechosos. |
| `sniffer_deffence.py` | Automatización de respuestas a incidentes. |
| `firewall_basic.sh`| Protege el sistema de ataques. |

### Instrucciones de Ejecución
```bash
sudo firewall_basic.sh #activa firewall
sudo python3 os_audit.py
sudo python3 alert_logger.py
sudo python3 sniffer_deffence.py
sudo ufw disable #desactiva el firewall
```

### Buenas Prácticas
- Mantener actualizado el sistema: `sudo apt update && sudo apt upgrade -y`.  
- Apagar la VM cuando no esté en uso.  
- Evitar exponer servicios innecesarios.  
- Usar contraseñas y claves seguras.  
- Supervisar accesos SSH desde IPs conocidas.  

---

## Red Team: Ataque y Evaluación de Seguridad

### Roles y Responsabilidades
- Simular ataques reales de ciberseguridad.  
- Identificar debilidades en la configuración de la VM.  
- Documentar hallazgos y proponer mejoras.  
- Automatizar escaneos y ataques con Python.  

### Configuración de la VM
- **Nombre:** RedTeam  
- **Región:** West US 3  
- **Imagen:** Ubuntu Server 24.04 LTS (x64)  
- **Tamaño:** Standard_D2s_v3 (2 vCPU, 8 GiB RAM)  
- **Puertos permitidos:** HTTP (80), HTTPS (443), SSH (22)  
- **Grupo de recursos:** RedTeam_group  

## Requisitos

### Software necesario

- Python 3.x
- pip (gestor de paquetes de Python)
- Nmap
- Acceso a Microsoft Azure (cuenta de estudiante)
### Librerias de Python

```bash
sudo apt install python3-scappy
sudo apt install python3-nmap
pip install paramiko
```
### Scripts Ofensivos
| Script            | Descripción |
|-------------------|-------------|
| `scanner.py`      | Escaneo de puertos y servicios con Nmap. |
| `packet_attack.py`| Sniffing y ARP/DNS Spoofing con Scapy. |
| `ssh_brute.py`    | Ataque de diccionario al servicio SSH con Paramiko. |
| `report.md`       | Documentación de hallazgos y recomendaciones. |

### Instrucciones de Ejecución
```bash
sudo python3 scanner.py
sudo python3 packet_attack.py
sudo python3 ssh_brute.py
```

### Evidencias
- Escaneo de puertos con Nmap: detección de SSH abierto en BlueTeam.  
- Ejecución de `ssh_brute.py`: acceso logrado con credenciales débiles.  
- Captura de tráfico sensible y generación de reportes.  

### Buenas Prácticas
- No ejecutar ataques fuera del entorno controlado.  
- Documentar cada paso y resultado.  
- Validar instalación de herramientas antes de pruebas.  
- Apagar la VM para conservar créditos de Azure.  

---

## Estructura del Proyecto
## 📂 Estructura del Proyecto

El proyecto se organiza en dos módulos principales: **Blue Team** (defensa) y **Red Team** (ataque).  
Cada módulo contiene scripts en Python y documentación asociada.

| Carpeta / Archivo       | Rol en el Proyecto | Descripción breve |
|--------------------------|-------------------|-------------------|
| `blue_team/`            | Defensa            | Scripts para monitoreo, auditoría y respuesta a incidentes. |
| ├── `monitor.py`        | Monitoreo          | Observa CPU, memoria y procesos en tiempo real. |
| ├── `log_audit.py`      | Auditoría          | Analiza logs del sistema para detectar anomalías. |
| ├── `alert.py`          | Alertas            | Envía notificaciones ante eventos sospechosos. |
| └── `response.py`       | Respuesta          | Automatiza acciones de mitigación frente a amenazas. |
| `red_team/`             | Ataque             | Scripts ofensivos para escaneo y explotación controlada. |
| ├── `scanner.py`        | Reconocimiento     | Escaneo de puertos y servicios con Nmap. |
| ├── `packet_attack.py`  | Ataques de red     | Sniffing y ARP/DNS spoofing con Scapy. |
| ├── `ssh_brute.py`      | Fuerza bruta       | Ataque de diccionario al servicio SSH. |
| └── `report.md`         | Documentación      | Informe de hallazgos y recomendaciones. |
| `README.md`             | Documentación raíz | Explica objetivos, roles, requisitos y resultados del proyecto. |

---

### 🔎 Notas sobre la organización
- **Separación clara de roles:** cada equipo tiene su propio espacio de trabajo.  
- **Scripts bien definidos:** cada archivo cumple una función específica (monitoreo, ataque, auditoría, etc.).  
- **Documentación integrada:** tanto el Blue Team como el Red Team cuentan con reportes y guías.  
- **Escalabilidad:** se pueden añadir más scripts sin perder orden, manteniendo la estructura modular.  


---

## Evaluación del Éxito
- **Red Team:** logró acceso no autorizado, identificó puertos inseguros y capturó tráfico sensible.  
- **Blue Team:** detectó intentos de ataque, generó alertas y aplicó respuestas automáticas.  
- **Resultado:** documentación clara de vulnerabilidades y defensas, con propuestas de mejora.  

---

## Conclusiones
Este proyecto permitió:
- Comprender la dinámica entre ofensiva y defensiva en ciberseguridad.  
- Aplicar herramientas de **Azure**, **Python** y librerías como `nmap`, `scapy`, `paramiko`, `psutil`.  
- Desarrollar habilidades prácticas en simulación de ataques y defensas en entornos cloud. 