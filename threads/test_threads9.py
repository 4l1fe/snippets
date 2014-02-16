import _thread, queue, time

numconsumers = 2
numproducers = 4
nummessages = 4

safeprint = _thread.allocate_lock()
dataqueue = queue.Queue()

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqueue.put('[producer id={} count={}]'.format(idnum, msgnum))

def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = dataqueue.get(block=False)
        except queue.Empty:
            print('empty')
        else:
            with safeprint:
                print('consumer', idnum, ' got', data)

if __name__ == '__main__':
    for i in range(numconsumers):
        _thread.start_new_thread(consumer, (i, ))
    for i in range(numproducers):
        _thread.start_new_thread(producer, (i, ))
    time.sleep(((numproducers-1)*nummessages) +1)
    print('MAIN EXITING')
