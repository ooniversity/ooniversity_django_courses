from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
	url(r'^$', 'courses.views.main', name='main'),
	url(r'^coaches/', include('coaches.urls')),
	url(r'^courses/', include('courses.urls')),
	url(r'^students/', include('students.urls', namespace="students")),
	url(r'^contact/$', 'pybursa.views.contact', name='contact'),
	url(r'^student_list/$', 'pybursa.views.student_list', name='student_list'),
	url(r'^student_detail/$', 'pybursa.views.student_detail', name='student_detail'),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :
	urlpatterns += patterns('django.contrib.staticfiles.views',
		url(r'^static/(?P<path>.*)$', 'serve'),
	)