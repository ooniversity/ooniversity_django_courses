from django.conf.urls import patterns, url
from students.views import student_list, student_detail


urlpatterns = patterns('',
    url(r'^$', student_list, name='student_list'),
    url(r'^(?P<student_id>\d+)/$', student_detail, name='student_detail'),
)
