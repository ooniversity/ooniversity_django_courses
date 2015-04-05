from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, contact, student_list, student_detail
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^contact/$', contact),
    url(r'^student_list/$', student_list),
    url(r'^student_detail/$', student_detail),

    url(r'^admin/', include(admin.site.urls)),
)
