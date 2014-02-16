import _thread, time

mutex = _thread.allocate_lock()
def counter(myID, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print('[{0}] => {1}'.format(myID, i))
        mutex.release()

for i in range(5):
    _thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print('main thread exiting')