import socket

print(socket.gethostname())
print(socket.gethostbyname('mojo'))
print(socket.gethostbyaddr('192.168.1.2'))
print(socket.getfqdn('google')) #full quality domain name
