from django.conf.urls import patterns, url

from views import course_info, add_lesson


urlpatterns = patterns('',     
     url(r'^(?P<course_id>\d+)/$', course_info, name='course_info'),
     url(r'^(?P<course_id>\d+)/add/', add_lesson, name='add_lesson'),
     )
