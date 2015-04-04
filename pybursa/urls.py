from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import pybursa, pybursa_contact, pybursa_student_list, pybursa_student_detail
 

urlpatterns = patterns('',
    url(r'^$', pybursa),
    url(r'^contact/$', pybursa_contact),
    url(r'^student_list/$', pybursa_student_list),
    url(r'^student_detail/$', pybursa_student_detail),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
