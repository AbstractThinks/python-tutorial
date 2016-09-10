# -*- coding: utf-8 -*-

from django.conf.urls import url
from index.views import get_index

urlpatterns = [
    url(r'^$', get_index, name='site_index')
]