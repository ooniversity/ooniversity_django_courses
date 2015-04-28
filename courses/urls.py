from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='course_info'),
    url(r'^(?P<pk>\d+)/add/', add_lesson, name='add_lesson'),
    url(r'^add/$', CourseCreateView.as_view(), name='add_course'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='edit_course'),
    url(r'^remove/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='remove_course'),
    )
