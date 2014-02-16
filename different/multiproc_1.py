import os
from multiprocessing import Process, RLock

def whoami(label, lock):
    msg = 'P{}: name:{}, pid:{}'
    with lock:
        print(msg.format(label, __name__, os.getpid()))

if __name__ == '__main__':
    lock = RLock()
    whoami('function call', lock)

    p = Process(target=whoami, args=('spawned child', lock))
    p.start()
    p.join()

    for i in range(5):
        Process(target=whoami, args=('run process {}'.format(i), lock)).start()

    with lock:
        print('main exit')