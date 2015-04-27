from django.conf.urls import patterns, url

from feedbacks.views import FeedbackCreateView


urlpatterns = patterns('',

    url(r'^feedback/$', FeedbackCreateView.as_view(), name = 'feedback-form'),

)
