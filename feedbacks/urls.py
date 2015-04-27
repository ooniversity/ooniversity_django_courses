from django.conf.urls import patterns, url
from feedbacks.views import ContactFormView, ContactCreateView

urlpatterns = patterns('',
                       url(r'^$', ContactCreateView.as_view(), name='message'),
)
