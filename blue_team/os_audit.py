#!/usr/bin/env python3
 
import pwd
import subprocess
from datetime import datetime
 
def list_users():
    print("\n--- Usuarios del sistema ---")
    for user in pwd.getpwall():
        if user.pw_uid >= 1000 and "nologin" not in user.pw_shell:
            print(f"Usuario: {user.pw_name}, Shell: {user.pw_shell}")
 
def list_open_ports():
    print("\n--- Puertos abiertos ---")
    try:
        result = subprocess.check_output(['ss', '-tuln'], text=True)
        print(result)
    except Exception as e:
        print(f"Error al listar puertos: {e}")
 
def list_services():
    print("\n--- Servicios activos ---")
    try:
        result = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--state=running'], text=True)
        print(result)
    except Exception as e:
        print(f"Error al listar servicios: {e}")
 
def log_event(message):
    with open("blue_team/log_events.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")
 
 
# -------------------------
# BLOQUE PRINCIPAL
# -------------------------
if _name_ == "_main_":
    print("Auditoría básica del sistema\n")
    log_event("Inicio de auditoría")
    list_users()
    log_event("Usuarios listados")
 
    list_open_ports()
    log_event("Puertos abiertos listados")
 
    list_services()
    log_event("Servicios activos listados")
 
    log_event("Fin de auditoría")