import logging
from concurrent.futures import ThreadPoolExecutor as Pool
from os import listdir
from os.path import splitext
from subprocess import call


logging.basicConfig(level=logging.INFO, format=("parent PID:%(process)05d %(threadName)-10s %(msg)s"))
logger = logging.getLogger(__name__)


def callback(future):
    if future.exception() is not None:
        logger.info("got exception: %s" % future.exception())
    else:
        logger.info("process returned %d" % future.result())


def main(max_workers):
    logger.info("begin")
    with Pool(max_workers=max_workers) as pool:
        for file in listdir('flv'):
            file = 'flv/'+file
            f = pool.submit(call, 'ffmpeg -loglevel quiet -y -i {0} -vcodec copy -acodec copy {1}.mp4'.format(file, splitext(file)[0]), shell=True)
            f.add_done_callback(callback)


if __name__=="__main__":
    import sys
    mw = int(sys.argv[1])
    main(mw)
