from django.conf.urls import patterns, include, url
from contact import views
from django.views.generic import TemplateView


urlpatterns = patterns( '',
    url(r'feedback/$', views.contact, name='feedback'),
    )
