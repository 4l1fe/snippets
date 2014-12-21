from toro import Queue
from tornado import gen

queue = Queue(maxsize=3)


@gen.coroutine
def producer():
    for item in range(5):
        print('pre produce [{}]'.format(item))
        yield queue.put(item)
        print('post produce [{}]'.format(item))


@gen.coroutine
def consumer():
    while True:
        item = yield queue.get()
        print('consumed [{}]'.format(item))


producer()
consumer()