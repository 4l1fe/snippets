# -*- coding: utf-8 -*-
import socket
import sys

#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', 10000) #принимает запросы от любого клиента

print('starting up on {sa[0]} port {sa[1]} '.format(sa=server_address), file=sys.stderr)

sock.bind(server_address)

while True:
    print('waiting to receive message', file=sys.stderr)
    data, address = sock.recvfrom(4096)
    print('received {0} from {1}'.format(len(data), address))
    print(data)
    if data:
        sent = sock.sendto(data, address)
        print('sent {0} bytes back to {1}'.format(len(data), address))

