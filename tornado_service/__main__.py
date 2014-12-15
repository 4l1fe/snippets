import time
import tornado
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

MAX_WORKERS = 4


class Handler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    # executor = ProcessPoolExecutor(max_workers=MAX_WORKERS)  # PicklingError: Can't pickle <type 'function'>:
                                                               #  attribute lookup __builtin__.function failed

    @run_on_executor
    def background_task(self, i):
        print('start task'+str(i))
        """ This will be executed in `executor` pool. """
        time.sleep(10)
        print('end task'+str(i))
        return i

    @tornado.gen.coroutine
    def get(self):
        """ Request that asynchronously calls background task. """
        idx = self.get_query_argument('idx')
        print('got request '+str(idx))
        res = yield self.background_task(idx)
        self.write(res)


HTTPServer(Application([("/", Handler)],debug=True)).listen(8888)
IOLoop.instance().start()