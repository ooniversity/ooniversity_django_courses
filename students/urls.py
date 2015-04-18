from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^/$', views.students, name='students'),
    url(r'/(?P<pk>\d+)/$', views.student_d, name='student_d'), 
)

