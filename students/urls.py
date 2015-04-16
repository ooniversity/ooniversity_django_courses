from django.conf.urls import patterns, url
from students.views import students, student_detail 

urlpatterns = patterns('',
	url(r'^$', students, name='students'),
	url(r'^(?P<student_id>\d+)/$', student_detail, name='student_detail'),
)