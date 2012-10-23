# coding: utf-8
"""
    Utility methods that are used in application
"""

from datetime import datetime
import imghdr
import os
from django.utils.crypto import random
from TestTask.settings import PROJECT_DIR


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
    """ Determines protocol type being used by request """

    return 'https' if request.is_secure() else 'http'


def is_valid_image(f):
    """ Determines if accepted file is an image """

    return imghdr.what(f) in ['png', 'gif', 'jpeg', 'bmp']


def handle_uploaded_file(f, id):
    """ Properly places and names uploaded file """

    if f is not None and is_valid_image(f):
        directory = os.path.join(PROJECT_DIR, 'static', 'images')
        file = open('%s/%s' % (directory, id), 'wb+')
        with file as destination:
            for chunk in f.chunks():
                destination.write(chunk)
