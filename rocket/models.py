from __future__ import unicode_literals
from django.db import models
import hashlib
import random
from django.contrib.auth.models import User
import datetime

class Tasks(models.Model):

    description = models.CharField(max_length=64)
    duration = models.IntegerField(default=0)
    registered = models.IntegerField(default=0)
    status = models.CharField(max_length=12,default="creada")
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.id) + self.description