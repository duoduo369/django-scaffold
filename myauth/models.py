# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def pre_save_user_handler(sender, instance, **kwargs):
    if settings.FEATURES.get('EMAIL_AS_USERNAME'):
        if not instance.email or instance.email.strip() != instance.username.strip():
            instance.email = instance.username
