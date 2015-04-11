from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<pk>\d+)/$', 'students.views.one_student', name='one_student'),
    url(r'^', 'students.views.detail', name='students_detail'),
)


