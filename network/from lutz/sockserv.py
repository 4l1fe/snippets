# -*- coding: utf-8 -*-
import os, sys
import socket
import pickle
import time

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind(('', 45555))
sockobj.listen(5)

#######
# новое
#######
ACTIVE_CHILDREN = []

def now():
    return time.ctime(time.time())

def reapChildren():
    while ACTIVE_CHILDREN:
        pid, stat = os.waitpid(0, os.WHOHANG)
        if not pid: break
        ACTIVE_CHILDREN.remove(pid)

def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = 'ECHO {} at {}'.format(data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)

def dispatcher():
    while True:
        connection, address = sockobj.accpet()
        print('Server connected by ', address, end=' ')
        print('at', now())
        reapChildren()
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)
        else:
            ACTIVE_CHILDREN.append(childPid)

dispatcher()


########
# старое
########
#while True:
#    connection, address = sockobj.accept()
#    print('connected from', address)
#
#    while True:
#        recv_data = connection.recv(1024)
#        if not recv_data: break
#        unpick_data = pickle.loads(recv_data)
#        print(unpick_data.get('nickname', 'unknow'), '>', unpick_data.get('message', 'unknow message'))
#        connection.send(b'Echo=>data recieved')
#    connection.close()
