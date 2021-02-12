import socket
import sys

print("Website Address: ")
hostname = input()
ip = socket.gethostbyname(hostname)
print('Hostname: ', hostname, '\n' 'IP: ', ip)