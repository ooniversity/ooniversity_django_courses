from django.conf.urls import patterns, url
from . import views
#from quadratic.views import *

urlpatterns = [
    url(r'^results/$', views.results_function, name='results_function'),
]
