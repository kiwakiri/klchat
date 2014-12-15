__author__ = 'Kip'
import socket

ip = '127.0.0.1'
port = 65532

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Hey Kip", (ip, port))
s.close()