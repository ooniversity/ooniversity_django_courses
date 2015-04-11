from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.stud_list, name='index'),
    url(r'^(?P<student_id>\d+)/', views.detail, name='detail'),
)
