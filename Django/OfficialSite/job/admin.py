from django.contrib import admin

# Register your models here.
from django.contrib import admin
from job.models import Category, Department, Address, Assortment, Job

admin.site.register([Category, Department, Assortment, Address, Job])
