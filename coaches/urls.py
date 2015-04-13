from django.conf.urls import patterns, include, url
from coaches import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<pk>\d+)/$', 'coaches.views.one_coach', name='one_coach'),
    #url(r'^', 'students.views.detail', name='students_detail'),
)


