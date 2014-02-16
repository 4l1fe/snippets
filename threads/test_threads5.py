import _thread, time


stdoutmutex = _thread.allocate_lock()
numthreads = 5
exitmutexes = [_thread.allocate_lock() for i in range(numthreads)]

def counter(myId, count, mutex):
    for i in range(count):
        time.sleep(1/(myId+1))
        with mutex:
            print('[{}] => {}'.format(myId, i))
    exitmutexes[myId].acquire()

for i in range(numthreads):
    _thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes):
    time.sleep(0.25)
print('main thread exiting')