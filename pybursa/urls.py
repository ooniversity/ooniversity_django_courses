from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from pybursa import views

urlpatterns = patterns('',

    #old url for task1
    #url(r'^$', views.index, name='index'),
    #url(r'^contact/$', views.contact, name='contact'),
    #url(r'^student_list/$', views.student_list, name='student_list'),
    #url(r'^student_detail/$', views.student_detail, name='student_detail'),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
