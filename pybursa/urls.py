from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa.views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
