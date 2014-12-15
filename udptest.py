__author__ = 'Kip'
import socket

ip = '192.168.1.109'
port = 65532
while 1:
    message = input("What do you want to type? ")
    if message == 'n':
        s.close()
        exit()
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(message, (ip, port))
s.close()