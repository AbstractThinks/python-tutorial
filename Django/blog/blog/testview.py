# -*- coding: utf-8 -*-

from django.http import HttpRequest

def first_page(req):
    return HttpRequest('<b>this is first test for template of the django</b>')