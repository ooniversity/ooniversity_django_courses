from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^1/$', views.course_plan),
)