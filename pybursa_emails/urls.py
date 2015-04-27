from django.conf.urls import patterns, include, url
from pybursa_emails.views import MailList, MailCreate, MailDelete

urlpatterns = patterns('pybursa_emails.views',

    url(r'^feedback/$', MailList.as_view(), name='feedback'),
    url(r'^mail_add/$', MailCreate.as_view(), name='mail_add'),
    url(r'^mail_rem/(?P<pk>\d+)/$', MailDelete.as_view(), name='mail_rem'),
    url(r'^mail/add/(?P<mail_id>\d+)/$', 'mail_add_redirect', name='mail_add_redirect'),
    url(r'^mail_send/(?P<mail_id>\d+)/$', 'mail_send', name='mail_send'),

)
