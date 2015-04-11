from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic.views import quadratic_results
from pybursa.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainP, name='home'),
    url(r'^polls/', include('courses.urls')),
	url(r'^contact/$', contact, name = 'contact'),
	#url(r'^student_list/$', stud_list, name = 'student_list'),
	#url(r'^student_detail/$', stud_detail, name = 'student_detail'),
	url(r'^courses/', include('courses.urls', namespace="courses")),
	url(r'^students/', include('students.urls', namespace="students")),
	url(r'^coaches/', include('coaches.urls', namespace="coaches")),
	# Examples:
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^quadratic/results', 'quadratic.views.quadratic_results', name = 'quadratic'),
    url(r'^admin/', include(admin.site.urls)),
)
