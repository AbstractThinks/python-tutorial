[django学习资料](http://www.code123.cc/575.html)


##基础命令

```python

#安装django
sudo easy_install django


#创建项目
django-admin.py startproject 项目名


#项目启动
#若不说明默认端口号为8000
python manage.py runserver 8080

#创建Django App
python manage.py startapp books

#更新数据库模型
python3.5 manage.py makemigrations 

#创建数据库关系映射
python manage.py migrate

#创建管理系统管理人员
python manage.py createsuperuser

```
注：在应用`settings.py`文件中的`MIDDLEWARE`配置项应改`为MIDDLEWARE_CLASSES`


##访问路径

```python

#urls.py
#添加url(r'^$', 'mysite.views.first_page')
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.first_page'),
)

就能访问到mysite/views.py文件中的first_page方法

```

##模块式开发

```python

#1.通过python manage.py startapp appName命令创建appName子模块

#2.修改主模块中setting.py文件，添加子模块

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appName',
)

#3.修改主模块中urls.py文件
#对于appName/的访问，要参考appName/urls.py
urlpatterns = patterns('',
 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.first_page'),
    url(r'^appName/', include('appName.urls')),
)

#4.静态文件访问
Django1.9

在setting.py文件中添加配置

```python
#在
#INSTALLED_APPS＝［
#	...
#	'django.contrib.staticfiles'
#	...
#］
#在STATIC_URL＝‘static’下添加配置
STATICFILES_DIR = (
	os.path.join(BASE_DIR, 'static'),
	'/static/目标目录'，#目标目录为可访问的静态资源文件夹
)
```


##创建模型

##模板

```python

#1.在项目根目录下创建templates文件夹并放入html模板

#2.修改主模块中settings.py文件，加入：

# Template dir
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/west/'),
)

#3.修改appName/views.py

# -*- coding: utf-8 -*- 
#from django.http import HttpResponse
from django.shortcuts import render
 
def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)
   #return render(request, 'templay.html', {'staffs': staff_list}) 

#4.模板循环语言

{% for item in staffs %}
<p>{{ item.id }}, {{item}}</p>
{% endfor %}

#5.模板选择语言

{% if condition1 %}
   ... display 1
{% elif condiiton2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}

#6.html继承（模板引擎）

{% extends "header.html" %}
 
{% block mainbody %}
 
{% for item in staffs %}
<p>{{ item.id }},{{ item.name }}</p>
{% endfor %}
 
{% endblock %}

```

##服务器搭配

```python

1.安装apache服务器和wsgi服务
例：
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi

2.在apache的配置文件/etc/apache2/apache2.conf中增加下面的配置：


Alias /media/ /home/vamei/media/    
Alias /static/ /home/vamei/static/ 
#在/home/vamei/static/中放入文件revenge.jpg，访问http://localhost/static/revenge

<Directory /home/vamei/static/>
Order deny,allow
Require all granted
</Directory>
 
<Directory /home/vamei/media/>
Order deny,allow
Require all granted
</Directory>

# Django
WSGIScriptAlias / /home/ubuntu/mysite/mysite/wsgi.py #是Django项目中自动创建的文件
WSGIPythonPath /home/ubuntu/mysite #Django项目所在的位置
 
<Directory /home/ubuntu/mysite/mysite>
<Files wsgi.py>
  Order deny,allow
  Require all granted
</Files>
</Directory>

```

完整实例 myblog
