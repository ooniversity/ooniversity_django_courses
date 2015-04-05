from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from pybursa import views as general_views


urlpatterns = patterns('',
	url(r'^$', general_views.dummy_render, name="home"),
	url(r'^contact/$', general_views.dummy_render, {'template': 'contact.html'}, name="contact"),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^students/', include('students.urls', namespace="students")),
	url(r'^student_list/$', RedirectView.as_view(url='/students/')),
	url(r'^student_detail/$', RedirectView.as_view(url='/students/1/')),
	url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
