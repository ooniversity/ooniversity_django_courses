from django.conf.urls import patterns, url

from views import students_on_course, student_info

urlpatterns = patterns('',  
	url(r'^(?P<student_id>\d+)/$', student_info, name='student_info'),
    url(r'^$', students_on_course, name='students_on_course'),    
    )





