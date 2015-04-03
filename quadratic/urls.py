from django.conf.urls import patterns, include, url
from quadratic.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', quadratic, name='quadratic'),
    url(r'^results/$', results, name='results'),
)
