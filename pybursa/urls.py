from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, contact


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
