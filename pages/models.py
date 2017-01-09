from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Faq(models.Model):
    """docstring for ClassName"""
    title = models.CharField("Title",max_length=100)
    text = models.CharField("Body",max_length=500)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title