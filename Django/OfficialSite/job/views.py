# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render, render_to_response
from job.models import Job, Address, Department
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_about_company(request):
    # ctx = {'Jobs':Job.objects.all().order_by('-created')}
    return render(request, 'job/index.html')

def get_about_job(request):
    return render(request, 'job/job.html')

def get_about_job_society(request):
    '''
    get_about_job_society
    :param request:
    :return:
    '''
    if request.method == 'GET':

        jobs_list = Job.objects.filter(assortment__name__exact='society')

        if request.GET.get('address'):
            jobs_list = jobs_list.filter(address__name__exact=request.GET.get('address'))
            print(jobs_list)
        if request.GET.get('depart'):
            jobs_list = jobs_list.filter(department__name__exact=request.GET.get('depart'))
        if request.GET.get('order') and request.GET.get('order') == 'up':
            print(1)
            jobs_list = jobs_list.order_by('created')
        else:
            print(2)
            jobs_list = jobs_list.order_by('-created')

        address = Address.objects.all()
        department = Department.objects.all()
        # jobs_list = Job.objects.filter(assortment__name__exact='society', address__name__exact='成都').order_by('-created')
        # jobs_list.order_by('-created')
        paginator = Paginator(jobs_list, 15)

        page = request.GET.get('page')


        try:
            jobs = paginator.page(page)
        except PageNotAnInteger:
            jobs = paginator.page(1)
        except EmptyPage:
            jobs = paginator.page(paginator.num_pages)

        ctx = {'Jobs' : jobs, 'Addresses' : address, 'Departments' : department}

        # ctx = {'Jobs': Job.objects.filter(assortment = 'school').order_by('-created')}
        return render(request, 'job/job_society.html', ctx)
    else:

        address = Address.objects.all()
        department = Department.objects.all()
        jobs = Job.objects.filter(assortment__name__exact='society', address__name__exact=request.POST['address']).order_by('-created')
        # paginator = Paginator(jobs_list, 15)
        #
        # page = request.GET.get('page')
        #
        # try:
        #     jobs = paginator.page(page)
        # except PageNotAnInteger:
        #     jobs = paginator.page(1)
        # except EmptyPage:
        #     jobs = paginator.page(paginator.num_pages)


        ctx = {'Jobs': jobs, 'Addresses': address, 'Departments': department}
        json_data = serializers.serialize("json", jobs)
        # ctx = {'Jobs': Job.objects.filter(assortment = 'school').order_by('-created')}

        return HttpResponse(json_data, content_type="application/json")

def get_about_job_school(request):
    jobs_list = Job.objects.filter(assortment__name__exact='school')

    if request.GET.get('address'):
        jobs_list = jobs_list.filter(address__name__exact=request.GET.get('address'))
        print(jobs_list)
    if request.GET.get('depart'):
        jobs_list = jobs_list.filter(department__name__exact=request.GET.get('depart'))
    if request.GET.get('order') and request.GET.get('order') == 'up':
        print(1)
        jobs_list = jobs_list.order_by('created')
    else:
        print(2)
        jobs_list = jobs_list.order_by('-created')

    address = Address.objects.all()
    department = Department.objects.all()
    # jobs_list = Job.objects.filter(assortment__name__exact='society', address__name__exact='成都').order_by('-created')
    # jobs_list.order_by('-created')
    paginator = Paginator(jobs_list, 15)

    page = request.GET.get('page')

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    ctx = {'Jobs': jobs, 'Addresses': address, 'Departments': department}
    return render(request, 'job/job_school.html', ctx)

def get_about_job_detail(request, job_id):
    try:
        job_detail = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        render(Http404)
    ctx = {'Job':job_detail}
    return render(request, 'job/job_detail.html',ctx)