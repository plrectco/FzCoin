import time
import re
import sys

from blockchain import Blockchain

def get_timestamp():
    return time.time()


def get_size(x):
    return sys.getsizeof(x)


def time_elapsed(timestamp):
    elapsed = get_timestamp() - timestamp
    if elapsed < 0:
        raise ValueError('Timestamp Incorrect.')
    return elapsed


def verify_email(email):
    EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
    if EMAIL_REGEX.match(email):
        return True
    else:
        return False


def verify_signature(text, signature, pk):
    pass


def verify_certificate(cert, root_CA):
    pass


def verify_blockchain(blockchain):
    pass


def lookup_pk(name):
    pass
