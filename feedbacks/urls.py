from django.conf.urls import patterns, include, url
from feedbacks.views import ContactFormView, ContactCreateView

urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name='contact_form'),
]

