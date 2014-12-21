import select


class IOLoop(object):

    def __init__(self, handlers=()):
        self.handlers = handlers

    def run(self):
        while True:
            wants_recv = [h for h in self.handlers if h.wants_to_receive()]
            wants_send = [h for h in self.handlers if h.wants_to_send()]
            can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
            for h in can_recv:
                h.handle_receive()
            for h in can_send:
                h.handle_send()