# -*- coding: utf-8 -*-
from myauth.models import UserProfile

import xadmin

class UserProfileAdmin(object):
    list_display = ('user', 'username', 'nickname', 'created_at')
    search_fields = ('user', 'user__email', 'username', 'nickname')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

xadmin.site.register(UserProfile, UserProfileAdmin)
