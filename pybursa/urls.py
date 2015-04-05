from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import mainP, contact, stud_list, stud_detail
from quadratic.views import quadratic_results

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainP, name='home'),
	url(r'^contact/$', contact, name = 'contact'),
	url(r'^student_list/$', stud_list, name = 'student_list'),
	url(r'^student_detail/$', stud_detail, name = 'student_detail'),
	# Examples:
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^quadratic/results', 'quadratic.views.quadratic_results', name = 'quadratic'),
    url(r'^admin/', include(admin.site.urls)),
)
