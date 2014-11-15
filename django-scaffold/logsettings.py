# -*- coding: utf-8 -*-
import os
import platform
import sys
from logging.handlers import SysLogHandler

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

def get_logger_config(debug=False, local_loglevel='INFO', console_loglevel=None, service_variant=None, syslog_addr=('localhost', 514)):
    '''
    debug: django settings debug
    syslog_addr: 远端syslog端口, tuple (ip, 514)
    '''

    if local_loglevel not in LOG_LEVELS:
        local_loglevel = 'INFO'

    if console_loglevel is None or console_loglevel not in LOG_LEVELS:
        console_loglevel = 'DEBUG' if debug else 'INFO'

    if service_variant is None:
        # default to a blank string so that if SERVICE_VARIANT is not
        # set we will not log to a sub directory
        service_variant = ''

    hostname = platform.node().split(".")[0]

    syslog_format = ("[service_variant={service_variant}]"
                     "[%(name)s] %(levelname)s "
                     "[{hostname}  %(process)d] [%(filename)s:%(lineno)d] "
                     "- %(message)s").format(service_variant=service_variant,
                                             hostname=hostname)
    handlers = ['console', 'local'] if debug else ['console', 'syslogger-remote', 'local']

    logger_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s %(levelname)s %(process)d '
                          '[%(name)s] %(filename)s:%(lineno)d - %(message)s',
            },
            'syslog_format': {'format': syslog_format},
            'raw': {'format': '%(message)s'},
        },
        'handlers': {
            'console': {
                'level': console_loglevel,
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'stream': sys.stderr,
            },
            'syslogger-remote': {
                'level': 'INFO',
                'class': 'logging.handlers.SysLogHandler',
                'address': syslog_addr,
                'formatter': 'syslog_format',
            },
        },
        'loggers': {
            '': {
                'handlers': handlers,
                'level': 'DEBUG',
                'propagate': False
            },
        }
    }
    if not debug:
        # for production environments we will only
        # log INFO and up
        logger_config['loggers']['']['level'] = 'INFO'
        logger_config['handlers'].update({
            'local': {
                'level': local_loglevel,
                'class': 'logging.handlers.SysLogHandler',
                'address': '/dev/log',
                'formatter': 'syslog_format',
                'facility': SysLogHandler.LOG_LOCAL0,
            },
            'tracking': {
                'level': 'DEBUG',
                'class': 'logging.handlers.SysLogHandler',
                'address': '/dev/log',
                'facility': SysLogHandler.LOG_LOCAL1,
                'formatter': 'raw',
            },
        })

    return logger_config
