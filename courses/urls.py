from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.course_info, name='course_info'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    url(r'^/add/$', views.course_add, name='course_add'),
    url(r'^edit/(?P<course_id>\d+)/$', views.course_edit, name='course_edit'),
    url(r'^remove/(?P<course_id>\d+)/$', views.course_remove, name='course_remove'),
)
