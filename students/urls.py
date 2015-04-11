from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<course_id>\d+)/$', views.linked_students, name='linked_students'),
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='detail'),
)
