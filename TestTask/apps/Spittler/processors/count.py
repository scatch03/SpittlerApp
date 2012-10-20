# coding: utf-8
"""
    Context processor for adding current count of spittles
"""

from TestTask.apps.Spittler.models import Spittle


def spittle_count(request):
    """ Count accessible now to every template by name spittle_count """

    return{
        'spittle_count': Spittle.objects.count()
    }
