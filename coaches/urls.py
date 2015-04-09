from django.conf.urls import patterns, url

from coaches.views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', CoachesView.as_view(), name='coaches'),
    url(r'^(?P<id>\d+)/$', CoachView.as_view(), name='coach'),
)
