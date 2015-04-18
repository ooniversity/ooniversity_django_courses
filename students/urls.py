from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^/$', views.students, name='students'),
    url(r'/(?P<pk>\d+)/$', views.student_d, name='student_d'),
    url(r'/add/$', views.add_stundent, name='add_stundent'),
    url(r'/edit/$', views.edit_student, name='edit_student'), 
)

