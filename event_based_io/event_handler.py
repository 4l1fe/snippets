import socket
from concurrent.futures import ThreadPoolExecutor


class EventHandler(object):

    def handle_send(self):
        pass

    def handle_receive(self):
        pass

    def wants_to_send(self):
        return False

    def wants_to_receive(self):
        return False

    def fileno(self):
        raise NotImplemented


class ThreadPoolHandler(EventHandler):

    def __init__(self, nworkers):
        self.signal_done_sock, self.done_sock = socket.socketpair()
        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)

    def fileno(self):
        return self.done_sock.fileno()

    def _complete(self, callback, future):
        self.pending.append((callback, future.result()))
        self.signal_done_sock.send(b'x')

    def run(self, func, args=(), kwargs={}, *, callback):
        future = self.pool.submit(func, *args, **kwargs)
        future.add_done_callback(lambda f: self._complete(callback, f))

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
        self.pending = []