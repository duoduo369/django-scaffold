# -*- coding: utf-8 -*-
from djangomako.shortcuts import render_to_response
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.error('error log test')
    logger.info('info log test')
    logger.debug('debug log test')
    return render_to_response('index.html', {})
