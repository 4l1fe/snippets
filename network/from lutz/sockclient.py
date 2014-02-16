# -*- coding: utf-8 -*-
import socket
import argparse
import pickle
import sys

#==========================================================#
#                      console keys                        #
#==========================================================#
parser = argparse.ArgumentParser(description='descrip of ArgumentParser class')

#parser.add_argument('-h',     action="store", dest='host')  # конфликт с ключом помощи -h/--help
parser.add_argument('--host', action="store", dest='host', required=True)

parser.add_argument('-p', '--port', action="store", dest="port", type=int,required=True)

#parser.add_argument('-m',        action="store", dest="message")
#parser.add_argument('--message', action="store", dest="message")

parser.add_argument('-nn', '--nickname', action="store", dest="nickname", required=True)
pars_res = parser.parse_args()

#==========================================================#
#                      socket object                       #
#==========================================================#
print(pars_res.host, pars_res.port)
sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((pars_res.host, pars_res.port))

while True:
    message = input(pars_res.nickname+' =>')
    if message in ['!q', '!e', '!exit', '!quit']:
        sys.exit('exit chat')
    nickname = pars_res.nickname

    data = {'nickname': nickname, 'message': message}
    sended_data = pickle.dumps(data, protocol=2)
    sockobj.send(sended_data)
    recv_data = sockobj.recv(1024)
    print('got from server:', recv_data)
sockobj.close()