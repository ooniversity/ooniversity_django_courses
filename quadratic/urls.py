from django.conf.urls import patterns, include, url

from quadratic.views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^old/$', quadratic_old, name='quadratic_old'),
    url(r'^results/$', results, name='results'),
    url(r'^old/results/$', results_old, name='results_old'),
)
