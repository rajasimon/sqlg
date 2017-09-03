"""
Data Generator Validator | Checks Datatime, String, Integer
"""
from datetime import datetime


def validate(date_text):
    """
    Python datetime validation utility function
    @argument: string date_text

    The program first convert this into datetime object. If the the program not
    able converting text to datetime then will throws error.
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")
