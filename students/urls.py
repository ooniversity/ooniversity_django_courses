from django.conf.urls import patterns, url
from students.views import student_list, student_detail, student_add


urlpatterns = patterns('',
    url(r'^$', student_list, name='student_list'),
    url(r'^(?P<student_id>\d+)/$', student_detail, name='student_detail'),
    url(r'^add/$', student_add, name='student_add'),
)
