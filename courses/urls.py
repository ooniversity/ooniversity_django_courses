from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.course_viev, name='course'),
)
