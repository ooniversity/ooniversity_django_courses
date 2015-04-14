from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *
from courses.views import courses_main



urlpatterns = patterns('',
	url(r'^$', courses_main, name='courses_main'),
	   
    url(r'^contact/', contact_list, name='contact_list'),
    url(r'^student_list/', student_list, name='student_list'),
    url(r'^student_detail/', student_detail, name='student_detail'),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),

    url(r'^courses/', include('courses.urls', namespace="courses")),    
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),           #####
    )
