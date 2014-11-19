# -*- coding: utf-8 -*-
from .settings import *

DEBUG = True
LOGGING = logsettings.get_logger_config(debug=DEBUG)

INSTALLED_APPS += (
    'app',
)
