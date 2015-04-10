from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns(
    '',
    url(r'^$', views.CourseView.as_view(), name='courses'),
    url(r'^(?P<id>\d+)/$', views.CourseDetialView.as_view(), name='detail'),
)
