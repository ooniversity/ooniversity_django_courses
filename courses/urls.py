from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.course_d, name='courses'), 
)
