from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^generator/(?P<test_exercice_pk>\d+)/$', views.generator, name='generator'),
    url(r'^generator/(?P<test_exercice_pk>\d+)/submit/$', views.generator_submit, name='generator_submit')
]
