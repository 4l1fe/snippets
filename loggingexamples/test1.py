# coding: utf-8
import logging

LOG_FILENAME = 'log.txt'
<<<<<<< HEAD
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, filemode='a')
=======
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, filemode='a', datefmt='%Y-%m-%d %H:%M:%S')
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078

logging.debug('Message go to log')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)