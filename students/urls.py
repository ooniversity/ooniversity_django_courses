from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns(
    '', url(r'^/$', views.students, name='students'),
    url(r'^(?P<pk>\d+)/$', views.student_d, name='student_d'),
    url(r'/add/$', views.add_student, name='add_student'),
    url(r'/edit/(?P<pk>\d+)/$', views.edit_student, name='edit_student'),
    url(r'/remove/(?P<pk>\d+)/$', views.remove_student, name='remove_student'),
)
