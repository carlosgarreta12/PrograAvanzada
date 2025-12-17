#!/usr/bin/env python3
import nmap
import os

info = []

scanner = nmap.PortScanner()

# Define target IP address or hostname
target = "20.228.97.25"

# Define Nmap options
options = "-sS -sV -Pn -T4 -O -A -p 1-1000"

# Run the Nmap scan with the specified options
scanner.scan(target, arguments=options)

# Print the scan results
for host in scanner.all_hosts():
    info.append(f"Host: {host}")
    info.append(f"State: {scanner[host].state()}")

    print("Host: ", host)
    print("State: ", scanner[host].state())

    for proto in scanner[host].all_protocols():
        info.append(f"Protocol: {proto}")

        print("Protocol: ", proto)

        ports = scanner[host][proto].keys()
        for port in ports:
            info.append(f"Port: {proto} State: {scanner[host][proto][port]['state']}")

            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])


path = os.getcwd()
file_name = 'report.txt'
abs_route = os.path.join(path, file_name)

with open(file_name, 'w', encoding='utf-8') as file:
    for line in info:
        file.write(line + "\n")