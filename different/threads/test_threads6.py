import threading


class MyThread(threading.Thread):

    def __init__(self, myid, count, mutex):
        self.myid = myid
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[{}] => {}'.format(self.myid, i))

stdoutmutex = threading.Lock()
threads = []
for i in range(10):
    thread = MyThread(i, 100, stdoutmutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print('MAIN EXITING')