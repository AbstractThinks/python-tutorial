from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def get_index(request):
    return render(request, 'index/index.html')
