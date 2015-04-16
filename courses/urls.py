from django.conf.urls import include, url, patterns
from django.contrib import admin
from courses import views

urlpatterns =  patterns('',
    # Examples:
    url(r'^/(?P<id>\d+)/$', views.show_course, name = 'course'),
    url(r'^/add/$', views.add_course, name='add_course'),
    url(r'^/edit/(?P<id>\d+)/$', views.edit_course, name='edit_course'),
    url(r'^/delete/(?P<id>\d+)/$', views.delete_course, name='delete_course'),
    url(r'^/(?P<id>\d+)/add_lesson', views.add_lesson, name = 'add_lesson'),
)