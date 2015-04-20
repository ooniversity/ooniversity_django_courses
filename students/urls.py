from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^add/$', views.student_add, name='student_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.student_edit, name='student_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.student_delete, name='student_delete'),
)
