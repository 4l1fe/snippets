# coding: utf-8
import argparse
import zerorpc
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, desc, Text
from sqlalchemy_utils import ChoiceType
from time import sleep
from random import uniform
from gevent import monkey; monkey.patch_all()
import gevent_psycopg2; gevent_psycopg2.monkey_patch()


Base = declarative_base()
OBJECT_TYPE_CONTENT = u'c'
OBJECT_TYPE_PERSON = u'p'
OBJECT_TYPE_MEDIA = u'm'
OBJECT_TYPE_MEDIA_UNIT = u'mu'
OBJECT_TYPE_STRIP = u's'
OBJECT_TYPE_TOPIC = u't'
OBJECT_TYPE_NEWS = u'n'
OBJECT_TYPES = (
    (OBJECT_TYPE_CONTENT, u'Контент'),
    (OBJECT_TYPE_PERSON, u'Персона'),
    (OBJECT_TYPE_MEDIA, u'Медиа'),
    (OBJECT_TYPE_MEDIA_UNIT, u'Медиаюнит'),
    (OBJECT_TYPE_STRIP, u'Лента'),
    (OBJECT_TYPE_NEWS, u'Новости'),
    (OBJECT_TYPE_TOPIC, u'Топик'),
)


class News(Base):
    __tablename__ = 'news'
    __table_args__ = {'extend_existing': True}

    id            = Column(Integer, primary_key=True)
    title      = Column(Text, nullable=True)
    comments_cnt  = Column(Integer, nullable=False)
    published     = Column(DateTime, nullable=True)
    created       = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    text          = Column(String(), nullable=False)
    obj_id        = Column(Integer, nullable=True)
    obj_name      = Column(String(256), nullable=True)
    obj_type    = Column(ChoiceType(OBJECT_TYPES), nullable=False)


class Service(object):

    def __init__(self):
        db = {'drivername': 'postgresql+psycopg2',
              'username': 'pgadmin',
              'password': 'qwerty',
              'host': 'localhost',
              'port': '5432',
              'database': 'next_tv'}
        self.engine = create_engine(URL(**db), pool_size=50)
        self.__Session = sessionmaker(bind=self.engine)

    def route(self, IPC_pack):
        route_s = self.__Session()
        # connection = self.engine.connect()
        print('connected ', route_s)
        print(self)
        time = 0.1
        resp = route_s.execute('''select pg_sleep({})'''.format(time))
        # resp = len(route_s.query(News).all())
        print('woke up ', route_s)
        # print(resp)
        # connection.close()
        route_s.close()
        return 'end'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--host', dest='host', default='127.0.0.1')
    parser.add_argument('-p', '--port', dest='port', default=6600)
    namespace = parser.parse_args()
    #
    server = zerorpc.Server(Service())
    server.bind("tcp://{host}:{port}".format(**vars(namespace)))
    print("start at {host}:{port}".format(**vars(namespace)))
    server.run()