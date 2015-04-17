from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa.views import index_ooniversity, contact


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^polls/', include('polls.urls', namespace = "polls")),


    # Load URLs page quadratic equation to basic parser URLs  [*??? Django Control 4 ???*]
    url(r'^quadratic/', include('quadratic.urls', namespace = "quadratic")),


    url(r'^$', index_ooniversity, name = 'index-ooniversity'),
    url(r'^contact/$', contact, name = 'contact'),

    url(r'^', include('students.urls', namespace = "students")),	# app - students
    url(r'^', include('courses.urls', namespace = "courses")),		# app - courses
    url(r'^', include('coaches.urls', namespace = "coaches")),		# app - coaches

)
