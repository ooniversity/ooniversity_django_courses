from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pybursa.views.dj101_index'),
    url(r'^contact/$', 'pybursa.views.dj101_contact'),
    url(r'^student_list/$', 'pybursa.views.dj101_student_list'),
    url(r'^student_detail/$', 'pybursa.views.dj101_student_detail'),
)
