from django.conf.urls import patterns, url
from quadratic.views import results


urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^results/$', results, name='results'),
)
