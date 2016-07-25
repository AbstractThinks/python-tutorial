
from django.conf.urls import url, patterns

urlpatterns = patterns('',
        url(r'^$', 'module.views.first_page'),
        url(r'^template', 'module.views.template'),
        url(r'^multi_templates', 'module.views.template2'),
        url(r'^for_templates', 'module.views.template3'),
        url(r'^extend_templates', 'module.views.template4'),
)
