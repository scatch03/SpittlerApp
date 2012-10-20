# coding: utf-8
"""
    Forms being used in spittler application
"""

from django import forms


class AddSpittleForm(forms.Form):
    """ User form for adding new spittle """

    subject = forms.CharField(max_length=120)
    message = forms.CharField(min_length=10, widget=forms.Textarea())
