import _thread
from threading import Timer

def output(tid, sec):
    print('from thread:  ', tid, ' sec=', sec)


def parent():
    i = 0
    while True:
        i += 1
        inp = input()
        if inp == 'q':
            break
        else:
            Timer(int(inp), output, [i, int(inp)]).start()
parent()