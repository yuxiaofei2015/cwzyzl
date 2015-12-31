# -*- coding=utf-8 -*-
from django.conf.urls import url
from . import views

"""
@author yxf
@contact yuxiaofei@youmi.net
@file urls.py.py
@create-time 15-12-23 下午3:20
"""
app_name = 'blog'

urlpatterns = [
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^addGroup/$', views.add_group, name='addGroup'),
    url(r'^create/$', views.create, name='create'),
    url(r'^detail/(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^group_manage/$', views.group_manage, name='group_manage'),
    url(r'^(?P<username>.+)/$', views.index, name='index'),
]
