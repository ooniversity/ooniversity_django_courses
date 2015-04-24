from django.conf.urls import patterns, include, url
from feedbacks.views import ContactFormView

urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name='contact_form'),
]

