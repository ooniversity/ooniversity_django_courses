from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pybursa.views import index, contact



urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    
    url(r'^admin/', include(admin.site.urls)),

)
