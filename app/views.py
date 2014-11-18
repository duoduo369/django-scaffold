# -*- coding: utf-8 -*-
import logging

from django.utils.translation import ugettext as _
from djangomako.shortcuts import render_to_response

logger = logging.getLogger(__name__)

def index(request):
    logger.error(_('error log test'))
    logger.info(_('info log test'))
    logger.debug(_('debug log test'))
    return render_to_response('index.html', {})
