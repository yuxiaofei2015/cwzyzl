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
    url(r'^$', views.index, name='index'),
]
