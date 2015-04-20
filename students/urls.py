from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',  
	url(r'^(?P<student_id>\d+)/$', student_info, name='student_info'),
    url(r'^$', students_on_course, name='students_on_course'),
    url(r'^add/$', add_student, name='add_student'),
    url(r'^edit/(?P<student_id>\d+)/$', edit_student, name='edit_student'),
    url(r'^remove/(?P<student_id>\d+)/$', remove_student, name='remove_student'),    
    )
