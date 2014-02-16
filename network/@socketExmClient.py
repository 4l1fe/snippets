# -*- coding: utf-8 -*-
import socket, sys, pprint

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Error code: '+msg[0]+', Error msg: '+msg[1])
    sys.exit()

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Could not be resolved')
    sys.exit()

sock.connect((remote_ip, port))
print('host - '+host+'; ip - '+remote_ip)

message = b"GET / HTTP/1.1\r\n\r\n"

try:
    sock.sendall(message)
except (socket.error, TypeError) as msg:
    print('Send failed')
    print(sys.exc_info()[1])
    sys.exit()

reply = sock.recv(4096)
pprint.pprint(reply)
#sock.close()