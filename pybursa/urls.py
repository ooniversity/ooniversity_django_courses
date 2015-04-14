from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *
from courses.views import *
from students.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contact/$', contact, name="contact"),
    url(r'^student_list/$', student_list, name="student_list"),
    url(r'^student_detail/$', student_detail, name="student_detail"),
    url(r'^$', courses_home_page, name="home"),
    url(r'^instructors/$', 'instructors.views.instructors_list', name="instructors_list"),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    #url(r'^instructors/', include('instructors.urls')),
)
