# coding: utf-8
"""
    Spittler Application Custom Textarea widget
"""

from django.forms import Textarea


class SpittleTextarea(Textarea):
    class Media:
        js = ('spittler/spittlerTextarea.js',)
        css = {
            'all': ('bootstrap/css/bootstrap.css',)
        }

    def __init__(self, language=None, attrs=None, **kwargs):
        attrs = {'class': 'spittler-textarea'}
        super(SpittleTextarea, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return super(SpittleTextarea, self).render(name, value, attrs)


