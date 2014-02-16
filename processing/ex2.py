#coding:utf-8
import os, time


def counter(count):
    for i in range(count):
        time.sleep(2)
        print('[{0}] => {1}'.format(os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('process {} spawned'.format(pid))
    else:
        counter(5)
        os._exit(0)

print('main process exiting')

