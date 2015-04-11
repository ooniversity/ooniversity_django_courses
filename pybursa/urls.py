from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import course, lesson_pd, lesson_js, lesson_rr
from students.views import student
 

urlpatterns = patterns('',
    url(r'^$', course, name='home'),
    url(r'^courses/1/$', lesson_pd, name='1'),
    url(r'^courses/2/$', lesson_js, name='2'),
    url(r'^courses/3/$', lesson_rr, name='3'),
    url(r'^students/$', student, name='student'),
    
    url(r'^polls/', include('polls.urls', namespace="polls")),
   
    url(r'^admin/', include(admin.site.urls)),
)
