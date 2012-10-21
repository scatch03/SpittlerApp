# coding: utf-8
"""
    Utility methods that are used in application
"""

from datetime import datetime
from django.utils.crypto import random


def slug_generator():
    """ Generates identification field for use inside of the system """

    current_date = datetime.now()
    return u'%04d%02d%02d%02d%02d%02d%03d' % (
        current_date.year, current_date.month,
        current_date.day, current_date.hour,
        current_date.minute, current_date.second,
        random.randint(0, 999)
    )


def get_protocol(request):
    return 'https' if request.is_secure() else 'http'
