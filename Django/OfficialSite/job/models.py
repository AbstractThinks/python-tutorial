# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models, migrations
class Category(models.Model):
    '''
    技术分类
    '''
    name = models.CharField('名称', max_length=32)
    def __unicode__(self):
        return self.name

# class Tag(models.Model):
#     '''
#     标签
#     '''
#     name = models.CharField('名称', max_length=32)

class Department(models.Model):
    '''
    部门
    '''
    name = models.CharField('名称', max_length=32)
    def __unicode__(self):
        return self.name
class Address(models.Model):
    '''
    地址
    '''
    name = models.CharField('名称', max_length=32)

    def __unicode__(self):
        return self.name
class Assortment(models.Model):
    '''
    招聘分类
    '''
    name = models.CharField('名称', max_length=32)
    def __unicode__(self):
        return self.name

class Job(models.Model):
    title = models.CharField('标题', max_length=128)
    created = models.DateTimeField('发布时间', auto_now_add=True)
    requirement = models.TextField('要求')
    responsibility = models.TextField('职责')
    description = models.TextField('描述')
    tag = models.TextField('标签')

    assortment = models.ForeignKey(Assortment, verbose_name='招聘分类', related_name='job_assortment')
    category = models.ForeignKey(Category, verbose_name='技术分类')
    address = models.ForeignKey(Address, verbose_name='地址')
    department = models.ForeignKey(Department, verbose_name='部门')

    def __unicode__(self):
        return self.title


