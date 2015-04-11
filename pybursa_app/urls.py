from django.conf.urls import patterns, include, url

urlpatterns = patterns('pybursa_app.views',
    url(r'^$', 'index', name='index'),
    url(r'^course/(?P<course_id>\d+)/$', 'course', name='course'),
    url(r'^student_list/(?P<course_id>\d+)/$', 'student_list', name='student_cours'),
    url(r'^contacts/$', 'contacts', name='contacts'),
    url(r'^student_list/$', 'student_list', name='student_list'),
    url(r'^student_detail/(?P<student_id>\d+)/$', 'student_detail',name='student_detail'),

)
