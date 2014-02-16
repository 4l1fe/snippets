import hashlib

db = dict(name1='123', name2='345', name3='dfg')
encrypted = {k: hashlib.sha512(v.encode()).hexdigest() for k, v in db.items()}

name = input('username:')
psw = input('password:')

if name not in encrypted or hashlib.sha512(psw.encode()).hexdigest() != encrypted.get(name):
    print('INCORRECT')
else:
    print('welcome')