from django.conf.urls import patterns, url
from students.views import students, student_detail, add_student, edit_student, delete_student 

urlpatterns = patterns('',
	url(r'^$', students, name='students'),
	url(r'^(?P<student_id>\d+)/$', student_detail, name='student_detail'),
	url(r'^add/$', add_student, name='student-adding'),
    url(r'^edit_student/(?P<pk>\d+)/$', edit_student, name='edit-student'),
    url(r'^delete_student/(?P<pk>\d+)/$', delete_student, name='delete-student'),
)