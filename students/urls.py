from django.conf.urls import patterns, url
from students.views import *


urlpatterns = patterns('',
    url(r'^$', students_all, name='index'),
    #url(r'^apply/$', apply_to_course, name='apply'),
    url(r'^add/$', add_student, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', edit_student, name='edit'), 
    url(r'^delete/(?P<pk>\d+)/$', delete_student, name='delete'), 
    url(r'^(?P<pk>\d+)/$', one_of_student, name='oneof'),
)