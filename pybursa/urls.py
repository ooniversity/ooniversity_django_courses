# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace = "polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace = "quadratic")),
    url(r'^$', views.show_index, name = 'index_itbursa'),
    url(r'^contact/$', views.show_contacts, name = 'contacts_itbursa'),
    url(r'^students/', include('students.urls', namespace = "students")),
    url(r'^courses/', include('courses.urls', namespace = "courses")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coaches/', include('coaches.urls', namespace = "coaches")),
    url(r'^feedback/', include('mails.urls', namespace = "mails")),
)
