from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='detail'),
)
