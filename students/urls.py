from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.student, name='students'),
    url(r'(?P<s_id>\d+)/$', views.get_student, name='get_student'),
)
