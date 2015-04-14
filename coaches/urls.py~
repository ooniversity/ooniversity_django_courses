from django.conf.urls import patterns, include, url
from students.views import *

urlpatterns = [
    url(r'^$', students_of_the_course, name='students_of_the_course'),
    url(r'^(?P<student_id>\d+)/$', student_info, name='student_info'),
]
