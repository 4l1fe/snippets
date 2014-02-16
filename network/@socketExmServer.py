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

    while True:
        data = conn.recv(1024)
        reply = b'OK '+data
        if not data:
            break

        conn.sendall(reply)

    conn.close()

while True:
    conn, addr = sock.accept()
    _thread.start_new_thread(clientthread, (conn,))

sock.close()
