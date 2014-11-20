# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class App(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=255, default='')
    desc = models.TextField()
    created_user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('view_app', u'查看app'),
        )
