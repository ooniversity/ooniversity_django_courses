from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
)
