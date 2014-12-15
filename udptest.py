__author__ = 'Kip'
import socket

ip = '127.0.0.1'
port = 65532
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = ''

while 1:
    message = input("What do you want to type? ")
    if message == 'n':
        s.close()
        exit()
    else:
        s.sendto(bytes(message, encoding='UTF-8'), (ip, port))
s.close()