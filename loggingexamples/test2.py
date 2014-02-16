import glob
import logging
import logging.handlers

LOG_FILENAME = 'log2.txt'
<<<<<<< HEAD
=======
logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5,)

my_logger.addHandler(handler)

for i in range(20):
    my_logger.debug('i = %d' % i)

logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print(filename)

