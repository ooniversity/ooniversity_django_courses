from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
#Change
urlpatterns = patterns('',
    url(r'^$', course_info, name='course_info'),
    url(r'^contact/', contact_list, name='contact_list'),
    url(r'^student_list/', student_list, name='student_list'),
    url(r'^student_detail/', student_detail, name='student_detail'),

    url(r'^polls/', include('polls.urls', namespace="polls")), #Might be deleted
    url(r'^admin/', include(admin.site.urls)),
)
