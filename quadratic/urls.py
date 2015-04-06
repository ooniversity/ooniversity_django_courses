from django.conf.urls import patterns, url

from quadratic.views import quadratic_results

urlpatterns = patterns('',

    # URL for page solutions quadratic equation
    url(r'^results/$', quadratic_results, name = 'result'),
)
