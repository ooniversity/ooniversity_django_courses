# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',

    #url(r'^$', views.IndexView.as_view(), name = 'index'),
    #URL для странички решения квадратного уравнения
    url(r'^results/$', views.quadratic_results, name = 'result'),

)

