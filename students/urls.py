from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^$', views.student, name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<question_id>\d+)/$', views.students_detail, name='detail'),
)
