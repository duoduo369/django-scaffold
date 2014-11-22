from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^fileupload$', 'app.views.fileupload', name='fileupload'),
)
