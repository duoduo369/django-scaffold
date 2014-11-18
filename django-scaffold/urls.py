# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django-scaffold.views.home', name='home'),
    # url(r'^django-scaffold/', include('django-scaffold.foo.urls')),
    url(r'', include('app.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

# 开启默认的admin
if settings.DEBUG or settings.FEATURES.get('ENABLE_DJANGO_ADMIN_SITE'):
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += (url(r'^admin/', include(admin.site.urls)),)

# 开启xadmin
if settings.DEBUG or settings.FEATURES.get('ENABLE_DJANGO_XADMIN_SITE'):
    import xadmin
    xadmin.autodiscover()
    # version模块自动注册需要版本控制的 Model
    urlpatterns += (url(r'xadmin/', include(xadmin.site.urls)),)
