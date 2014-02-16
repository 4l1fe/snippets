import socket
import sys

#полное соединение
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], 10000)
print('connecting to {sa[0]} port {sa[1]}'.format(sa=server_address))
sock.connect(server_address)
try:
    message = b'some ZZZ words'
    print('sending {0}'.format(message), file=sys.stderr)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {0}'.format(data))
finally:
    sock.close()

#простое соединение
#def get_constans(prefix):
#    return dict( (getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix))
#
#families = get_constans('AF_')
#types = get_constans('SOCK_')
#protocols = get_constans('IPPROTO_')
#
#sock = socket.create_connection(('localhost', 10000))
#print(sock.type)
#print(sock.family)
#print(sock.proto)
#
#try:
#    message = b'some ZZZ words'
#    print('sending {0}'.format(message))
#    sock.sendall(message)
#
#    amount_received = 0
#    amount_expected = len(message)
#
#    while amount_received < amount_expected:
#        data = sock.recv(16)
#        amount_received += len(data)
#        print('received {0}'.format(data))
#finally:
#    print('closing socket', file=sys.stderr)
#sock.close()