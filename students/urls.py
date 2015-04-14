from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.student, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.student_detail, name='detail'),
)
