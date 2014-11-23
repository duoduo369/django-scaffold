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
    'EMAIL_AS_USERNAME': False, # 使用邮箱做用户名
    'USE_YUN_STORAGE': False,
    'ENABLE_SOCIAL_AUTH': False, # 启用三分登陆
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

# django默认的 TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
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
#
# 如果有其他AUTHENTICATION_BACKENDS的配置，在settings.py最下面重写

if FEATURES.get('ENABLE_SOCIAL_AUTH'):

    if FEATURES.get('EMAIL_AS_USERNAME'):
        assert 0, u'你启用了EMAIL_AS_USERNAME请自行配置下面的backends'

    INSTALLED_APPS += (
        'social_auth',
    )
    #######################  oauth  ###################################

    AUTHENTICATION_BACKENDS = (
        # 去掉注释开启下面的oauth
        #'social_auth.backends.contrib.douban.Douban2Backend',
        #'social_auth.backends.contrib.qq.QQBackend',
        #'social_auth.backends.contrib.weibo.WeiboBackend',
        #'social_auth.backends.contrib.renren.RenRenBackend',
        #'social_auth.backends.contrib.baidu.BaiduBackend',
        #'social_auth.backends.contrib.weixin.WeixinBackend',
        'django.contrib.auth.backends.ModelBackend',
        # 使用EMAIL_AS_USERNAME, 注释掉 django.contrib.auth.backends.ModelBackend
        # 解开下行的注释, 去掉上面的assert 0
        # 'myauth.backends.EmailAuthBackend',
    )


    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.contrib.auth.context_processors.auth',
        # login in htemplate can use "{% url socialauth_begin 'douban-oauth2' %}"
        'social_auth.context_processors.social_auth_by_type_backends',
        'social_auth.context_processors.social_auth_login_redirect',
    )


    SOCIAL_AUTH_PIPELINE = (
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.partial.save_status_to_session',
        'social.pipeline.social_auth.save_authentication_user_detail_to_session',
    )
    # 注意我在SOCIAL_AUTH_PIPELINE并没有使用文档里面的一些pipeline
    # 因为文档中的pipeline会在新auth的时候创建新的django用户，当使用
    # 邮箱作为名字的时候搞不定, 因此我将注册流程从默认的SOCIAL_AUTH_PIPELINE中截断,
    # (有时候你想在三分用户输入用户名密码成功回跳后让用户绑定邮箱之类的),
    # 重写了django-social-auth使得在SOCIAL_AUTH_AUTHENTICATION_SUCCESS_URL
    # 的sessions中将三方返回的信息都放在一个叫做authentication_user_detail的
    # request.session.get('authentication_user_detail')
    # 之后根据这些信息来创建用户等等满足你自己注册需求


    SOCIAL_AUTH_DISCONNECT_PIPELINE = (
        # Verifies that the social association can be disconnected from the current
        # user (ensure that the user login mechanism is not compromised by this
        # disconnection).
        'social.pipeline.disconnect.allowed_to_disconnect',
        # Collects the social associations to disconnect.
        'social.pipeline.disconnect.get_entries',
        # Revoke any access_token when possible.
        'social.pipeline.disconnect.revoke_tokens',
        # Removes the social associations.
        'social.pipeline.disconnect.disconnect'
    )

    SOCIAL_AUTH_LOGIN_URL = '/login-url'
    SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error'
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in'
    SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url'
    SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url'
    SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url'
    SOCIAL_AUTH_AUTHENTICATION_SUCCESS_URL = '/authentication_success_url'

    SOCIAL_AUTH_WEIBO_KEY = ''
    SOCIAL_AUTH_WEIBO_SECRET = ''

    SOCIAL_AUTH_QQ_KEY = ''
    SOCIAL_AUTH_QQ_SECRET = ''

    SOCIAL_AUTH_DOUBAN_OAUTH2_KEY = ''
    SOCIAL_AUTH_DOUBAN_OAUTH2_SECRET = ''

    SOCIAL_AUTH_RENREN_KEY = ''
    SOCIAL_AUTH_RENREN_SECRET = ''

    SOCIAL_AUTH_BAIDU_KEY = ''
    SOCIAL_AUTH_BAIDU_SECRET = ''

    SOCIAL_AUTH_WEIXIN_KEY = ''
    SOCIAL_AUTH_WEIXIN_SECRET = ''
    SOCIAL_AUTH_WEIXIN_SCOPE = ['snsapi_login',]


try:
    from .local_settings import *
except ImportError:
    pass
