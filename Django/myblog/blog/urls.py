# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views import get_blogs, get_detail

urlpatterns = [
    url(r'^$',get_blogs, name='blog_get_blogs' ),
    url(r'^detail/(\d+)/$', get_detail, name='blog_get_detail'),
]