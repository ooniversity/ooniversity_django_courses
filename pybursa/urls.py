from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^contact/', views.contact),
    url(r'^student_list/', views.student_list),
    url(r'^student_detail/', views.student_detail),
    url(r'^admin/', include(admin.site.urls)),
)
