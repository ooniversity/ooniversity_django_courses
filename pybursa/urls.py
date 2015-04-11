from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa.views import index, contact, student_detail, student_list

from pybursa.views import ooniversity, course, students, student_info


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^polls/', include('polls.urls', namespace = "polls")),


    # Load URLs page quadratic equation to basic parser URLs  [*??? Django Control 4 ???*]
    url(r'^quadratic/', include('quadratic.urls', namespace = "quadratic")),


    # Ooniversity site pages - Django Control 5
    url(r'^$', ooniversity, name = 'ooniversity'),

    url(r'^courses/(?P<id_course>\d+)/$', course),
    url(r'^students/(?P<id_stud>\d+)/$', student_info, name = 'student_info'),
    url(r'^students/$', students, name = 'students'),


    # PyBursa site pages - Django Control 3
    #url(r'^$', index, name = 'index'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^student_detail/$', student_detail, name = 'student_detail'),
    url(r'^student_list/$', student_list, name = 'student_list'),

)
