from django.conf.urls import patterns, include, url

urlpatterns = patterns('pybursa_app.views',
    url(r'^$', 'index'),
    url(r'^contact/$', 'contacts'),
    url(r'^student_list/$', 'student_list'),
    url(r'^student_detail/$', 'student_detail'),
)
