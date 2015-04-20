from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from pybursa import views

urlpatterns = patterns('',
                       url(r'^polls/',
                           include('polls.urls', namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='index'),

                       url(r'^courses/',
                           include('courses.urls', namespace='courses')),
                       url(r'^coaches/',
                           include('coaches.urls', namespace='coaches')),

                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^students/',
                           include('students.urls', namespace='students')),

                       url(r'^quadratic/',
                           include('quadratic.urls', namespace='quadratic')),

                       )
