from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),

    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),

    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),

    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^students/', include('students.urls')),

    url(r'^courses/', include('courses.urls')),


)
