# coding: utf-8
# from utils.connection import create_session, db_connect, mongo_connect
import argparse
import zerorpc
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from time import sleep
from gevent import monkey; monkey.patch_all()
# from gevent import sleep, spawn, joinall
# from green_sqla import make_psycopg_green;make_psycopg_green()
import gevent_psycopg2; gevent_psycopg2.monkey_patch()


class Service(object):

    def __init__(self):
        db = {'drivername': 'postgresql+psycopg2',
              'username': 'postgres',
              'password': 'postgres',
              'host': 'localhost',
              'port': '5432',
              'database': 'postgres'}
        self.engine = create_engine(URL(**db))
        self.connection = self.engine.connect()

    def route(self):
        print('connected')
        # sleep(10)
        resp = self.connection.execute('''select pg_sleep(10)''')
        print('woke up')
        # row = resp.fetchone()
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
