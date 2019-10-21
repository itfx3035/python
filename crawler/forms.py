# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class document_form(forms.Form):
    file = forms.FileField(
        label='Select a file'        
    )