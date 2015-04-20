from django.conf.urls import patterns, include, url
from students.views import *

urlpatterns = [
    url(r'^$', students_of_the_course, name='students_of_the_course'),
    url(r'^(?P<student_id>\d+)/$', student_info, name='student_info'),
    url(r'^add/$', add_edit_student, name='add_student'),
    url(r'^edit/(?P<student_id>\d+)/$', add_edit_student, name='edit_student'),
    url(r'^delete/(?P<student_id>\d+)/$', delete_student, name='delete_student'),
]

