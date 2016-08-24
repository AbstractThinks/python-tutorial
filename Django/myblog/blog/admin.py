from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Category, Tag, Blog

admin.site.register([Category, Tag, Blog])
