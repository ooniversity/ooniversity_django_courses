from django.conf.urls import patterns, include, url

from feedback import views

urlpatterns = patterns('',
    url(r'^$', views.FeedbackCreateView.as_view(), name='feedback'),
)