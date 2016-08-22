from django.shortcuts import render
import json

# Create your views here.
from django.template import loader,Context
from django.http import  HttpRequest
from article.models import BlogPost

def test(request):
    return render(request, 'test.html')

def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', {'posts' : posts})