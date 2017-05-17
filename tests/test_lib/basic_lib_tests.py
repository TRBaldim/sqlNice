import time
import string
import numpy as np


def str_time_prop(start, end, date_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, date_format))
    etime = time.mktime(time.strptime(end, date_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(date_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d-%m-%Y', prop)


def random_word(length):
    array_of_chars = list(string.ascii_lowercase)
    return ''.join(np.random.choice(array_of_chars) for _ in range(length))
