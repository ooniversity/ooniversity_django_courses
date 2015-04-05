from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'pybursa.views.index', name='index'),
    url(r'^contact/$', 'pybursa.views.contact', name='contact'),
    url(r'^student_list/$', 'pybursa.views.student_list', name='student_list'),
    url(r'^student_detail/$', 'pybursa.views.student_detail', name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
