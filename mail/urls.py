from django.conf.urls import url, patterns
from mail import views

urlpatterns =  patterns('',
    # Examples:
    url(r'^$', views.MailCreateView.as_view(), name='feedback'),

)
