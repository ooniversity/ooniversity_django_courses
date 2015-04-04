from django.conf.urls import patterns, include, url
from django.contrib import admin
import pybursa  


urlpatterns = patterns('',
    url(r'^$', 'pybursa.views.index', name='home'),
	url(r'^index/$', 'pybursa.views.index', name='home'),
    url(r'^contact/$', 'pybursa.views.contact'),
	url(r'^student_list/$', 'pybursa.views.student_list'),
	url(r'^student_detail/$', 'pybursa.views.student_detail'),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
