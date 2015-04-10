from django.conf.urls import patterns, url

from students.views import students_all, student_info

urlpatterns = patterns('',
    url(r'^$', students_all, name='students_all'),
    url(r'^(?P<student_id>\d+)/$', student_info, name='student_info'),
    #url(r'^(?P<pk>\d+)/$', student, name='student'),
    #url(r'^(?P<course_id>\d+)/$', views.vote, name='vote'),
)