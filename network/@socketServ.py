import socket
import sys

#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on {sa[0]} port {sa[1]} '.format(sa=server_address), file=sys.stderr)
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for coonection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(16)
            print('received', data, file=sys.stderr)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()


