import socket
import sys

sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_name = sys.argv[1]
server_address = (server_name, 10000)
message = 'by DATAGRAM'.encode()

try:
    print('sending message')
    sent = sock.sendto(message, server_address)

    print('waiting to receive')
    data, address = sock.recvfrom(4096)
    print('received {0}'.format(data))

finally:
    sock.close()
