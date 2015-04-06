from django.conf.urls import patterns, include, url

urlpatterns = patterns('pybursa_app.views',
    url(r'^$', 'index', name='index'),
    url(r'^contacts/$', 'contacts', name='contacts'),
    url(r'^student_list/$', 'student_list', name='student_list'),
    url(r'^student_detail/$', 'student_detail',name='student_detail'),
)
