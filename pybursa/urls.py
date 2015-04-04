from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, contact, student_l, student_d

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^contact/$', contact, name ='contact'),
    url(r'^student_list/$', student_l, name='student_l'),
    url(r'^student_detail/$', student_d, name = 'student_d'),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
