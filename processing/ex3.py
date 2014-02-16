#coding:utf-8
import os

parm = 0
while True:
    parm +=1
    pid = os.fork()
    print(pid)
    if pid == 0:
        os.execlp('python', 'python', 'child.py', str(parm))
        assert False, 'error starting programm'
    else:
        print('child is', pid)
        if input() == 'q': break
