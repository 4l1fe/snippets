# coding: utf-8
import argparse
import zerorpc
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from time import sleep
from random import uniform
from gevent import monkey; monkey.patch_all()
import gevent_psycopg2; gevent_psycopg2.monkey_patch()


class Service(object):

    def __init__(self):
        db = {'drivername': 'postgresql+psycopg2',
              'username': 'postgres',
              'password': 'postgres',
              'host': 'localhost',
              'port': '5432',
              'database': 'postgres'}
        self.engine = create_engine(URL(**db), pool_size=50)

    def route(self, IPC_pack):
        connection = self.engine.connect()
        print('connected ', connection)
        time = uniform(0.01, 0.02)
        resp = connection.execute('''select pg_sleep({})'''.format(time))
        print('woke up ', connection)
        connection.close()
        return 'end'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', default='127.0.0.1')
    parser.add_argument('--port', dest='port', default=6600)
    namespace = parser.parse_args()
    #
    server = zerorpc.Server(Service())
    server.bind("tcp://{host}:{port}".format(**vars(namespace)))
    print("start at {host}:{port}".format(**vars(namespace)))
    server.run()
