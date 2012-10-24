# coding: utf-8
"""
    Custom template tags common to whole project
"""

from django import template
from TestTask.apps.spittler.models import Spittle

register = template.Library()


def render_spittle(identity):
    """ Preparing data for tag template using spittle identity """
    spittle = Spittle.objects.get(_slug=identity)
    return {
        'spittle': spittle,
    }

register.inclusion_tag('render_spittle.html')(render_spittle)
