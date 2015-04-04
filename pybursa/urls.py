#this is pybursa urls!
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'contacts/', ContactView.as_view(), name='contacts'),
    url(r'student_list', StudentListView.as_view(), name='studlist'),
    url(r'student_detail', StudentDetailView.as_view(), name='studdet'),
)



