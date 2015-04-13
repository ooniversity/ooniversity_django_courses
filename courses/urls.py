from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<course_id>\d+)/$', views.course_detail, name='detail'),
)
