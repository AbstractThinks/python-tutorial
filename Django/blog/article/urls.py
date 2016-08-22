# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from article import views


urlpatterns = [
    url(r'^$', views.archive),
    url(r'^test', views.test)
]