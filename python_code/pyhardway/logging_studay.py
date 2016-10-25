import argparse

parser = argparse.ArgumentParser(description='I print fibonacci sequence')
parser.add_argument('-s', '--start', type=int, dest='start',
    help='Start of the sequence', required=True)
parser.add_argument('-e', '--end', type=int, dest='end',
    help='End of the sequence', required=True)
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='Enable debug info')


import logging

logger = logging.getLogger('fib')
logger.setLevel(logging.DEBUG)

hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)

logger.addHandler(hdr)


def infinite_fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        logger.debug('Before caculation: a, b = %s, %s' % (a, b))
        logger.debug('After caculation: a, b = %s, %s' % (a, b))
        yield b

def fib(start, end):
    for cur in infinite_fib():
        logger.debug('cur: %s, start: %s, end: %s' % (cur, start, end))
        if cur > end:
            return
            if cur >= start:
                logger.debug('Returning result %s' % cur)
                yield cur


def main():
    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)

    for n in fib(args.start, args.end):
        print(n)



if __name__ == '__main__':
    main()
