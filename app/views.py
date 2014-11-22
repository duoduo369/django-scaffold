# -*- coding: utf-8 -*-
import logging
import os

from time import time
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST
from djangomako.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from utils.http import JsonResponse
from utils.storage import storage

logger = logging.getLogger(__name__)

def index(request):
    logger.error(_('error log test'))
    logger.info(_('info log test'))
    logger.debug(_('debug log test'))
    context = {}
    context.update(csrf(request))
    return render_to_response('index.html', context)


@require_POST
def fileupload(request):
    js = {'success': False}
    f = request.FILES.get('file')
    if not f:
        return JsonResponse(js)
    file_name = gen_upload_file_name(f.name)
    handle_uploaded_file(file_name, f)
    js['success'] = True
    return JsonResponse(js)


def handle_uploaded_file(name, content):
    '''
    name -- 文件名
    content -- file obj
    '''
    storage.save(name, content)


def gen_upload_file_name(name):
    '''
    生成文件名
        用时间戳来做, 如果有扩展名则加扩展名
    '''
    new_name = str(time()).replace('.' , '')
    if '.' in name:
        suffix = name.split('.')[-1]
    if suffix:
        new_name = '{}.{}'.format(new_name, suffix)
    return new_name
