import socket
import time
from event_handler import EventHandler, ThreadPoolHandler
from ioloop import IOLoop


class UDPServer(EventHandler):

    def __init__(self, address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(address)

    def fileno(self):
        return self.socket.fileno()

    def wants_to_receive(self):
        return True


class UDPTimeServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.socket.recvfrom(1)
        self.socket.sendto(time.ctime().encode('ascii'), addr)


class UDPEchoServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.socket.recvfrom(8192)
        self.socket.sendto(msg, addr)


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


class UDPFibServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.socket.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n,), callback=lambda r: self.respond(r, addr))

    def respond(self, result, addr):
        self.socket.sendto(str(result).encode('ascii'), addr)


if __name__ == '__main__':
    # IOLoop((UDPTimeServer(('', 14000)), UDPEchoServer(('', 15000)))).run()
    pool = ThreadPoolHandler(4)
    IOLoop((pool, UDPFibServer(('', 16000)))).run()