# -*- coding: utf-8 -*- 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^bbs/', include('bbs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'web.post.views.home', name='home'),
    url(r'^account/reg/$', 'web.usr.views.register', name='reg'),
    url(r'^account/setting/$', 'web.usr.views.setting', name='setting'),
    url(r'^account/login/$', 'web.usr.views.login'),
    url(r'^account/logout/$', 'web.usr.views.logout', name='logout'),
    url(r'^post/(?P<post_id>\d+)/$', 'web.post.views.get'),
    url(r'^post/create/$', 'web.post.views.create'),
    url(r'^post/(?P<post_id>\d+)/del$', 'web.post.views.delete'),
    url(r'^comment/create/$', 'web.comment.views.create'),
) + staticfiles_urlpatterns()