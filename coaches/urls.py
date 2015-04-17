from django.conf.urls import patterns, url

from coaches.views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', CoachesView.as_view(), name='coaches'),
    url(r'^(?P<pk>\d+)/$', CoachView.as_view(), name='coach'),
    url(r'^add/$', coach_add, name='coach_add'),
    url(r'^edit/(?P<pk>\d+)/$', coach_edit, name='coach_edit'),
    url(r'^remove/(?P<pk>\d+)/$', coach_remove, name='coach_remove'),
    url(r'^adduser/$', user_add, name='user_add'),
)
