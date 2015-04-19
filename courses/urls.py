from django.conf.urls import patterns, url
from courses import views


urlpatterns = patterns('',
    url(r'^(?P<c_id>\d+)/$', views.course, name='courses'),
    url(r'^add/$', views.add_course, name='add_course'),
    url(r'^edit/(?P<id>\d+)/$', views.edit_course, name='edit_course'),
    url(r'^remove/(?P<id>\d+)$', views.remove_course, name='remove_course'),
    url(r'^(?P<id>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
)
