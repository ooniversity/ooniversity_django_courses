from django.conf.urls import patterns, url
from feedbacks.views import ContactCreateView

urlpatterns = patterns('',
                       url(r'^$', ContactCreateView.as_view(), name='message'),
)
