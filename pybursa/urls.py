from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index_ooniversity, contact
#from courses.views import course, lesson_pd, lesson_js, lesson_rr, add_lesson
#from feedbacks.views import feedback

 

urlpatterns = patterns('',
    #url(r'^$', course, name='home'),
    #url(r'^courses/1/$', lesson_pd, name='1'),
    #url(r'^courses/2/$', lesson_js, name='2'),
    #url(r'^courses/3/$', lesson_rr, name='3'),
    #url(r'^students/$', student, name='student'),
    #url(r'^add_lesson/$', add_lesson, name='add_lesson'),

    url(r'^$', index_ooniversity, name='home'),
    url(r'^contact/$', contact, name='contact'),
    
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^', include('students.urls', namespace='students')),
    url(r'^', include('coaches.urls', namespace='coaches')),
    url(r'^', include('courses.urls', namespace='courses')), 
    url(r'^', include('feedbacks.urls', namespace="feedbacks")),
    url(r'^admin/', include(admin.site.urls)),
)
