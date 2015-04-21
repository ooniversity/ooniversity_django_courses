from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.stud_list, name='index'),
    url(r'^add/$', views.apply_to_course, name='add'),
    url(r'^registred/$', views.registred, name='registred'),
    url(r'^(?P<student_id>\d+)/', views.detail, name='detail'),
    url(r'^edit/(?P<pk>\d+)/', views.edit_from_course, name='edit'),
    url(r'^delete/(?P<pk>\d+)/', views.delete_from_course, name='delete'),
)
