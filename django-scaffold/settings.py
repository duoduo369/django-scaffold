# -*- coding: utf-8 -*-
# Django settings for django-scaffold project.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

FEATURES = {
    'ENABLE_DJANGO_ADMIN_SITE': True,
    'ADMIN_LIB': 'xadmin', # 可以在 xadmin, admin中选择，admin
                           # 二者不能同时使用，admin的用法看文档
                           # xadmin的Admin集成自object,
                           # register时使用xadmin.site.register
                           # 文件放在 adminx.py 而不是admin.py
    'USE_SQLITE3': False,
    'EMAIL_AS_USERNAME': True,
    'USE_YUN_STORAGE': False,
}

#   启用EMAIL_AS_USERNAME: True后会使用 email作为用户名
#   实际上就是将user的username = email, 其他的用户名之类的请放到profile里面
#   https://github.com/dabapps/django-email-as-username
#
#   from emailusernames.utils import create_user, create_superuser
#
#   create_user('me@example.com', 'password')
#   当然也可以知己诶把user的username设置为email就ok了
#   create_superuser('admin@example.com', 'password')
#   from emailusernames.utils import get_user, user_exists
#
#   user = get_user('someone@example.com')
#   ...
#
#   if user_exists('someone@example.com'):
#       ...
#
#

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'myauth.UserProfile'

# db config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

if FEATURES.get('USE_SQLITE3'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev.db',
        }
    }

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        }
    }


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

LANGUAGES = (
    # ('en', 'English'),
    ('zh-cn', 'Simplified Chinese'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias') # 如果不用云存储使用绝对路径

if FEATURES.get('USE_YUN_STORAGE'):
    MEDIA_ROOT = 'medias' # 云存储使用这种相对路径

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'statics') # 如果不用云存储使用绝对路径

if FEATURES.get('USE_YUN_STORAGE'):
    STATIC_ROOT = 'statics' # 云存储使用这种相对路径

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_dev"),
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@lba)zukbwoe1yx#!3g5!9i_ti-6dyw=!3zmfl@kh31e2(=6^0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'custom_django_partial.middleware.HttpResponseNotAllowedMiddleware',
    'djangomako.middleware.MakoMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'django-scaffold.urls'


STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django-scaffold.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'south',
    'ecstatic',
    'myauth', # 自定义权限相关的东西放在这里
    'app', # clone后默认的小demo
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
from . import logsettings

LOGGING = logsettings.get_logger_config(debug=DEBUG)

# memcached
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "utils.memcache.safe_key",
        "KEY_PREFIX": "memcached_default",
        "TIMEOUT": str(60 * 3),
        "LOCATION": [
            "localhost:11211"
        ],
    },
}

# FEATURES
# 开启admin
if FEATURES.get('ADMIN_LIB', '') == 'admin':
    if DEBUG or FEATURES.get('ENABLE_DJANGO_ADMIN_SITE'):
        INSTALLED_APPS += (
            'django.contrib.admin',
        )

# 开启xadmin
if FEATURES.get('ADMIN_LIB', '') == 'xadmin':
    if DEBUG or FEATURES.get('ENABLE_DJANGO_ADMIN_SITE'):
        INSTALLED_APPS += (
            'xadmin',
            'crispy_forms',
        )

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

if FEATURES.get('EMAIL_AS_USERNAME'):

    AUTHENTICATION_BACKENDS = (
        'myauth.backends.EmailAuthBackend',
    )

# 如果你有其他的AUTHENTICATION_BACKENDS请加在这里
# 如果你有非常复杂的AUTHENTICATION_BACKENDS顺序
# 请直接重写这个tuple，但是注意EMAIL_AS_USERNAME的这个FEATURE
# 如果启用这个FEATURE, 需要关掉django默认的Backend，默认用email
#    AUTHENTICATION_BACKENDS = (
#        'emailusernames.backends.EmailAuthBackend',
#        # Uncomment the following to make Django tests pass:
#        # 'django.contrib.auth.backends.ModelBackend',
#    )
AUTHENTICATION_BACKENDS += ()

ECSTATIC_MANIFEST_FILE = os.path.join(BASE_DIR, 'staticmanifest.json')

# 个人配置或者一些不想丢到git里面的配置
if FEATURES.get('USE_YUN_STORAGE'):
    # 默认选择七牛
    # Doc: https://github.com/duoduo369/django-qiniu-storage
    QINIU_ACCESS_KEY = ''
    QINIU_SECRET_KEY = ''
    QINIU_BUCKET_NAME = ''
    QINIU_BUCKET_DOMAIN = ''

    # 下面这两行是指在七牛云里面静态文件没有hash码
    DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
    # STATICFILES_STORAGE  = 'qiniustorage.backends.QiniuStaticStorage'
    # 下面这这行是指在七牛云里面添加hash码, 注意只要静态文件这个
    STATICFILES_STORAGE  = 'custom_django_partial.storages.QiniuCachedStaticStorage'


try:
    from .local_settings import *
except ImportError:
    pass
