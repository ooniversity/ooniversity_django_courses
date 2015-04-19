from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),

    url(r'^$', index, name='index'),
    #url(r'^course_add/$', course_add, name='course_add'),
    #url(r'^course_edit/(?P<course_id>\d+)/$', course_edit, name='course_edit'),
    #url(r'^course_delete/(?P<course_id>\d+)/$', course_delete, name='course_delete'),

    url(r'^contact/$', contact, name='contact'),

    url(r'^student_list/$', student_list, name='student_list'),#obsolete
    url(r'^student_detail/$', student_detail, name='student_detail'),#obsolete

    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^courses/', include('courses.urls', namespace='courses')),

)
