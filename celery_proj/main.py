from __future__ import absolute_import
import logging
from celery import Celery
from datetime import timedelta
from logging.handlers import RotatingFileHandler
from os.path import join


app = Celery('main',
             broker='amqp://',
             backend='amqp://')
app.conf.update(CELERY_TASK_RESULT_EXPIRES=3600,
                CELERY_REDIRECT_STDOUTS=False,
                CELERYBEAT_SCHEDULE={
                    'add-every-10-seconds': {
                        'task': 'task1',
                        'schedule': timedelta(seconds=5)
                    },
                    'add-ever-10-seconds': {
                        'task': 'task_from_schedule',
                        'schedule': timedelta(seconds=5),
                        'args': ('text from schedule', )
                    },
                    'add-ever-3-seconds': {
                        'task': 'gui_task',
                        'schedule': timedelta(seconds=5)
                    },
                })


CELERY_TASKS_LOG_DIR = '.'


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        rfh = RotatingFileHandler(join(CELERY_TASKS_LOG_DIR, name), maxBytes=2048)
        logger.addHandler(rfh)
    logger.setLevel(logging.DEBUG)
    return logger


@app.task(name='task1', bind=True)
def task_1(self):
    logger = get_logger(self.name)
    logger.info(repr(logger))
    logger.info(repr(vars(logger)))
    logger.info('WWWW')


@app.task(name='task_from_schedule', bind=True)
def from_schedule(self, arg):
    logger = get_logger(self.name)
    logger.info(repr(logger))
    logger.info(repr(vars(logger)))
    logger.info('ZZZ')


@app.task(name='gui_task', bind=True)
def from_schedule(self):
    logger = get_logger(self.name)
    logger.info(repr(logger))
    logger.info(repr(vars(logger)))
    logger.info('AAA')