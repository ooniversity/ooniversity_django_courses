from django.conf.urls import patterns, include, url
from django.contrib import admin
# import students
# import courses

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    # url(r'^courses/', include('courses.urls')),
    
    url(r'^$', 'courses.views.index', name='home'),
    url(r'^courses/', include('courses.urls')),
    url(r'^contact/', 'students.views.contact', name='contact'),
    url(r'^students/', 'students.views.student_list', name='student_list'),
    url(r'^student_detail/', include('students.urls')),
    url(r'^coach/', include('coaches.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
