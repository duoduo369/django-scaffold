# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class UserProfile(models.Model):
    '''
    username: 用户名是唯一的，可以为Null
    nickname: 昵称是可以变的，可以重复
    '''
    user = models.OneToOneField(User, unique=True, related_name='profile')
    username = models.CharField(blank=True, null=True, unique=True, max_length=255)
    nickname = models.CharField(blank=True, max_length=255, db_index=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "auth_userprofile"


@receiver(pre_save, sender=User)
def pre_save_user_handler(sender, instance, **kwargs):
    '''
    保存用户前如果开启了EMAIL_AS_USERNAME, 需要将email字段设为username
    '''
    if settings.FEATURES.get('EMAIL_AS_USERNAME'):
        if not instance.email or instance.email.strip() != instance.username.strip():
            instance.email = instance.username

@receiver(post_save, sender=User)
def post_save_user_handler(sender, instance, created, **kwargs):
    profile = UserProfile(user=instance)
    profile.save()

@receiver(pre_save, sender=UserProfile)
def pre_save_userprofile_handler(sender, instance, **kwargs):
    '''
    保存profile前，如果用户名为空，则设置为None, 躲避unique检查
    '''
    if not instance.username:
        instance.username = None
