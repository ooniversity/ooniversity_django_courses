# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from mails import views


urlpatterns = patterns('',

    url(r'^$', views.MailCreateView.as_view(), name = 'send-mail'),

)
