# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class mdocument(models.Model):
    doc_name = models.CharField(max_length=1000)    

class murl(models.Model):
    doc_id = models.ForeignKey(mdocument, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    url_alive = models.BooleanField(default=False)
    