__author__ = 'Kip'

import socket

print("holy fuck, we\'re writing shit")

port = 65532
ip = "127.0.0.1"

'''
Server listens for connection on UDP 65532
When it receives a packet, send packet back to acknowledge connection
'''

sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((ip, port))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    temp = data.decode()
    print('Received message: ' + data + '\n' + 'From: ' + addr[0])
