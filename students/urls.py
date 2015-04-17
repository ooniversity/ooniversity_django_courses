from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.students_all, name='students_all'),
    url(r'^(?P<student_id>\d+)/$', views.student_info, name='student_info'),
    url(r'^add/$', views.student_add, name='student_add'),
    url(r'^edit/(?P<student_id>\d+)/$', views.student_edit, name='student_edit'),
    url(r'^remove/(?P<student_id>\d+)/$', views.student_remove, name='student_remove'),
)