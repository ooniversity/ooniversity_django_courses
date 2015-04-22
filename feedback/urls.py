from django.conf.urls import patterns, url
from feedback.views import FeedbackMessageCreateView


urlpatterns = patterns('',
    url(r'^$', FeedbackMessageCreateView.as_view(), name='message'),
)
