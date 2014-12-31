# -*- coding: utf-8 -*-
from functools import wraps

from django.core.cache import cache


def cache_if_anonymous(view_func):
    """ 
    Many of the pages in edX are identical when the user is not logged
    in, but should not be cached when the user is logged in (because
    of the navigation bar at the top with the username).

    The django middleware cache does not handle this correctly, because
    we access the session to put the csrf token in the header. This adds
    the cookie to the vary header, and so every page is cached seperately
    for each user (because each user has a different csrf token).

    Note that this decorator should only be used on views that do not
    contain the csrftoken within the html. The csrf token can be included
    in the header by ordering the decorators as such:

    @cache_if_anonymous
    def myView(request):
    """
    @wraps(view_func)
    def _decorated(request, *args, **kwargs):
        if not request.user.is_authenticated():
            #Use the cache
            # same view accessed through different domain names may
            # return different things, so include the domain name in the key.
            domain = str(request.META.get('HTTP_HOST')) + '.'
            cache_key = domain + "cache_if_anonymous." + request.path
            response = cache.get(cache_key)
            if not response:
                response = view_func(request, *args, **kwargs)
                cache.set(cache_key, response, 60 * 3)

            return response

        else:
            #Don't use the cache
            return view_func(request, *args, **kwargs)

    return _decorated


class CacheResponse(object):
    '''
    这个decorator是缓存django restframework的response的。
    '''
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
