import socket

host = input("Enter hostname: ")

try:
    ip = socket.gethostbyname(host)
    print("IP address of", host, "is", ip)
except socket.gaierror:
    print("Hostname not found!")
