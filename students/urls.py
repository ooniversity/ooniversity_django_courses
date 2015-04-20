from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.student, name='students'),
    url(r'^(?P<s_id>\d+)/$', views.get_student, name='get_student'),
    url(r'^add/$', views.add_student, name='add_student'),
    url(r'^edit/(?P<id>\d+)/$', views.edit_student, name='edit_student'),
    url(r'^remove/(?P<id>\d+)/$', views.remove_student, name='remove_student'),
)
