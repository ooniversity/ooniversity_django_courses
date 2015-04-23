from django.conf.urls import include, url, patterns
from django.contrib import admin
from courses import views

urlpatterns =  patterns('',
    # Examples:
    url(r'^/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name = 'course'),
    url(r'^/add/$', views.CourseCreateView.as_view(), name='add_course'),
    url(r'^/edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit_course'),
    url(r'^/delete/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='delete_course'),
    url(r'^/(?P<id>\d+)/add_lesson', views.add_lesson, name = 'add_lesson'),
)