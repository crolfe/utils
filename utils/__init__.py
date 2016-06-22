import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.WARN)

# Version
VERSION = (0, 0, 1)


def get_version():
    return '{}.{}.{}'.format(VERSION[0], VERSION[1], VERSION[2])
