# -*- coding: utf-8 -*-
from django.conf.urls import url

from job.views import get_about_company, get_about_job, get_about_job_school,get_about_job_society,get_about_job_detail

urlpatterns = [
    url(r'^about', get_about_company, name='site_about_company'),
    url(r'^$', get_about_job, name='site_about_job'),
    url(r'^society', get_about_job_society, name='site_about_job_society'),
    url(r'^school', get_about_job_school, name='site_about_job_school'),
    url(r'^detail/(\d+)/$', get_about_job_detail, name='site_about_job_detail'),
]