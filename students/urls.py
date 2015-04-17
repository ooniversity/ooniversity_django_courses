from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render
from views import students_list, student_info

urlpatterns = patterns('',
                       url(r'^$', students_list, name="students_list"),
                       url(r'^(?P<id>\d)/$', student_info,
                           name="student_detail"),
                       )
