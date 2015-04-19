from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render
from views import course_info, lesson_adding

urlpatterns = patterns('',
                       url(r'^(?P<id>\d+)/$', course_info, name="courseinfo"),
                       url(r'^(?P<id>\d+)/add_lesson/$', lesson_adding, name="lesson_add"),
                       
                       )
