from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='detail'),
    url(r'^add/', views.student_add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.student_edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.student_remove, name='remove'),
)
