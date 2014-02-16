import _thread
import time


def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        print('[{}] => {}'.format(myId, i))

for i in range(5):
    _thread.start_new_thread(counter, (i, 5))

time.sleep(6)

print('main thread exiting')