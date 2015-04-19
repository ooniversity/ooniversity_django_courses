from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.course_d, name='courses'),
    url(r'add/$', views.add_course, name='add_course'),
    url(r'edit/(?P<pk>\d+)/$', views.edit_course, name='edit_course'),
    url(r'remove/(?P<pk>\d+)/$', views.remove_course, name='remove_course'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
)
