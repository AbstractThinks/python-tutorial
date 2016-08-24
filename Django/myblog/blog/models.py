from django.db import models, migrations
from django import forms


# Create your models here.
class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField('名称', max_length=16)

class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField('名称', max_length=16)

class Blog(models.Model):
    '''
    博客
    '''

    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

class Comment(models.Model):
    '''
    评论
    '''

    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
    created = models.DateTimeField('发布时间', auto_now_add=True)

class CommentForm(forms.Form):

    '''
    评论表单
    '''

    name = forms.CharField(label='称呼', max_length=16, widget=forms.TextInput(attrs={'class' : 'form-control'}), error_messages={
        'required' : '请填写你的邮箱',
        'max_length' : '称呼太长'
    })

    email = forms.EmailField(label='邮箱', widget=forms.TextInput(attrs={'class' : 'form-control'}), error_messages={
        'required' : '请填写您的邮箱',
        'invalid' : '邮箱格式不对'
    })
    content = forms.CharField(label='评论内容', widget=forms.Textarea(attrs={'class' : 'form-control'}), error_messages={
        'required' : '请填写您的评论内容',
        'max_length' : '评论内容太长'
    })






'''
blog详情页面
'''
# class Migration(migrations.Migration):
#     initial = True
#     dependencies = []
#     operations = [
#         migrations.CreateModel(
#             name='Blog',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('title', models.CharField(max_length=32, verbose_name='标题')),
#                 ('author', models.CharField(max_length=16, verbose_name='作者')),
#                 ('content', models.TextField(verbose_name='正文')),
#                 ('created', models.DateTimeField(auto_created=True, verbose_name='发布时间')),
#             ],
#         )
#     ]