# -*- coding: utf-8 -*-
from django.core.cache import cache
from functools import wraps

class CacheResponse(object):
    def __init__(self, timeout=60*3, key_func=None):
        self.timeout = timeout
        self.key_func = self.default_calculate_key if not key_func else key_func
        self.cache = cache

    def default_calculate_key(self, view_instance, view_method, request, args, kwargs):
        domain = str(request.META.get('HTTP_HOST')) + '.'
        cache_key = domain + "cache_api_response." + request.path
        return cache_key

    def __call__(self, func):
        this = self
        @wraps(func)
        def inner(self, request, *args, **kwargs):
            return this.process_cache_response(
                view_instance=self,
                view_method=func,
                request=request,
                args=args,
                kwargs=kwargs,
            )
        return inner

    def process_cache_response(self, view_instance, view_method, request, args, kwargs):
        key = self.calculate_key(
            view_instance=view_instance,
            view_method=view_method,
            request=request,
            args=args,
            kwargs=kwargs
        )
        response = self.cache.get(key)
        if not response:
            response = view_method(view_instance, request, *args, **kwargs)
            response = view_instance.finalize_response(request, response, *args, **kwargs)
            response.render()  # should be rendered, before picklining while storing to cache
            self.cache.set(key, response, self.timeout)
        if not hasattr(response, '_closable_objects'):
            response._closable_objects = []
        return response

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        key_func = self.key_func
        return key_func(
            view_instance=view_instance,
            view_method=view_method,
            request=request,
            args=args,
            kwargs=kwargs,
        )

cache_response = CacheResponse
