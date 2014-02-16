<<<<<<< HEAD
# -*- coding: utf-8 -*-
#не рабочий
import socket, sys
import threading, _thread

HOST = ''
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((HOST,PORT))
except socket.error as msg:
    print(msg)
    sys.exit()

sock.listen(10)
def clientthread(conn):
    conn.send(b'Welcome to the server. Type something and hit enter\n')
=======
import socket, sys
import threading, _thread

ADDR = ('localhost', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)
sock.listen(10)

clients = []
while True:
    conn, addr = sock.accept()
    clients.append(conn)
    for clint in clients:
        conn.send(b'Welcome to the server. Type something and hit enter\n')
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078

    while True:
        data = conn.recv(1024)
        reply = b'OK '+data
        if not data:
            break
<<<<<<< HEAD

        conn.sendall(reply)

    conn.close()

while True:
    conn, addr = sock.accept()
    _thread.start_new_thread(clientthread, (conn,))

=======
        conn.sendall(reply)
    conn.close()

>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
sock.close()
