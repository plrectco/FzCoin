import time
import re

def get_timestamp():
    return time.time()


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
