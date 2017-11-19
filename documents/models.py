# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Revision(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    owner = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    attachment = models.CharField(max_length=400)
    activated_date = models.DateTimeField('Date Activated')
    removed_date = models.DateTimeField('Date Superseded / Archived')
