from django.conf.urls import patterns, url
from feedbacks.views import  *

urlpatterns = patterns('',
url(r'^feedback/$', add_feedback, name = 'feedback'),
)