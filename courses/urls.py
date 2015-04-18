from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.course_d, name='courses'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    url(r'^(?P<pk>\d+)/edit_lesson/$', views.edit_lesson, name='edit_lesson'),
    url(r'^(?P<pk>\d+)/remove_lesson/$', views.remove_lesson, name='remove_lesson'), 
)
