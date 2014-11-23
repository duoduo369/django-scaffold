# -*- coding: utf-8 -*-
from django.contrib import admin

from app.models import App
import xadmin

class AppAdmin(object):
    list_display = ('name', 'desc', 'created_user', 'created_at')
    search_fields = ('title', 'desc', 'created_user')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

xadmin.site.register(App, AppAdmin)
