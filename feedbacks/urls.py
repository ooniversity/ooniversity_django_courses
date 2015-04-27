from django.conf.urls import patterns, url
from feedbacks import views

urlpatterns = patterns('',
    url(r'^$', views.MessageFeedbackCreateView.as_view(), name='feedback'),


)
