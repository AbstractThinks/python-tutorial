#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_page(req):
    return HttpResponse("<p>西餐</p>")

def template(req):

    # 需要在主模块的setting配置文件的配置TEMPLATES才能访问到模版
    context = {}
    context['label'] = 'Hello World'
    return render(req, 'first.html', context)


def template2(req):

    context = {}
    context = {'label1':'Hello','label2':'jesse'}
    return render(req, 'first2.html', context)

def template3(req):
    
    context = {}
    context['items'] = [{"name":"jesse"},{"name":"vicy"}]
    return render(req, 'first3.html', context)

def template4(req):
    return render(req, 'first5.html',{})
def template5(req):
    pass
def template6(req):
    pass
