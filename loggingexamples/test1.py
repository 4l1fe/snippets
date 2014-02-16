# coding: utf-8
import logging

LOG_FILENAME = 'log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, filemode='a')

logging.debug('Message go to log')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)