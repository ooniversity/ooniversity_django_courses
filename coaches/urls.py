from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('',
    #url(r'^(?P<course_id>\d+)/$', views.detail_studs, name='curs_stud'),
    url(r'^(?P<coach_id>\d+)/$', views.detail, name='coaches'),
)
