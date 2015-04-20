from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('pybursa_app.urls', namespace="pybursa_app")),
    url(r'^', include('courses.urls', namespace="courses")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
)
