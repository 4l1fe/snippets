import _thread


stdoutmutex = _thread.allocate_lock()
exitmutexes = [_thread.allocate_lock() for i in range(10)]
#exitmutexes = [False] * 10

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[{}] => {}'.format(myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()
#    exitmutexes[myId] = True

for i in range(10):
    _thread.start_new_thread(counter, (i, 100))

for mutex in exitmutexes:
    while not mutex.locked(): pass

#while False in exitmutexes: pass
print('main thread exiting')