from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.course_view, name='course'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    url(r'^add/$', views.course_add, name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.course_edit, name='course_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.course_delete, name='course_delete'),
)
