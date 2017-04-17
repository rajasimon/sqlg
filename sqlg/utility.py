""" Helper module """
import json
import time
import random
import string


def read_file(filename):
    return json.loads(open(filename).read())

def random_integer(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def process_data(data):
    """ Takes data as input and will return important values from file """
    # Table Name from Json file
    table_name = data['table_name']

    # No of Column
    column_count = data['column_count']

    # No of Row
    row_count = data['row_count']

    # Table columns schema from Json file
    column_properties = data['column_properties']

    # Get the row row_properties
    row_properties = data['row_properties']
    return table_name, column_count, row_count, column_properties, row_properties


def string_time_proportion(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return string_time_proportion(start, end, '%Y-%m-%d %H:%M:%S', prop)