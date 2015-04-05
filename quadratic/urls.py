from django.conf.urls import patterns, include, url

urlpatterns = patterns('quadratic.views',
    url(r'^results/', 'resolve'),

)
