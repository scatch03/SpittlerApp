# coding: utf-8
"""
    Forms being used in spittler application
"""

from django import forms
from TestTask.apps.Spittler.widgets.SpittleTextarea import SpittleTextarea


class AddSpittleForm(forms.Form):
    """ User form for adding new spittle """

    subject = forms.CharField(max_length=120)
    message = forms.CharField(min_length=10, widget=SpittleTextarea())
    file = forms.FileField(label='', required=False)