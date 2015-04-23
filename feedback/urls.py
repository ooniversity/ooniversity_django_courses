from django.conf.urls import patterns, include, url

from feedback import views


urlpatterns = patterns(
    '',
    url(r'^$', views.FeedbackView.as_view(), name='feedbacks'),
)
