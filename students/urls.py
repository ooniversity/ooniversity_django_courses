from django.conf.urls import patterns, url

from students import views


urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
)
