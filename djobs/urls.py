# -*- coding: utf-8 -*-
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(('djobs.views'),
    # Examples:
    # url(r'^$', 'djobs.views.home', name='home'),
    # url(r'^djobs/', include('djobs.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^$', include('simpleblog.urls')),
)

urlpatterns += patterns((''),
    url(r'^simpleblog/', include('simpleblog.urls')),
)

urlpatterns += patterns((''),
    #静态文件
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}
            # {'document_root': '/home/gs/djobs/static/'}
    ),
)