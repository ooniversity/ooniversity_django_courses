from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.student, name='index'),
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='detail'),
    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^edit_student/(?P<pk>\d+)/$', views.edit_student, name='edit_student'),
    url(r'^delete_student/(?P<pk>\d+)/$', views.delete_student, name='delete_student'),
)
