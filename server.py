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

tester = bytes('hey', encoding='UTF-8')
print(tester.decode(encoding='UTF-8'))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print('Received message: ' + data.decode(encoding='UTF-8') + '\n' + 'From: ' + addr[0])
