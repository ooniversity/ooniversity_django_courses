from django.conf.urls import patterns, include, url

urlpatterns = patterns('pybursa_app.views',
    url(r'^$', 'index', name='index'),
    url(r'^course/(?P<course_id>\d+)/$', 'course', name='course'),
    url(r'^coach/(?P<coach_id>\d+)/$', 'coach', name='coach'),
    url(r'^student_list/(?P<course_id>\d+)/$', 'student_list', name='student_cours'),
    url(r'^contacts/$', 'contacts', name='contacts'),
    url(r'^student_list/$', 'student_list', name='student_list'),
    url(r'^student_add/$', 'student_add', name='student_add'),
    url(r'^student_mod/(?P<student_id>\d+)/$', 'student_mod', name='student_mod'),
    url(r'^student_rem/(?P<student_id>\d+)/$', 'student_rem', name='student_rem'),
    url(r'^student_detail/(?P<student_id>\d+)/$', 'student_detail',name='student_detail'),
    url(r'^student/mod/(?P<student_id>\d+)/$', 'student_mod_redirect', name='student_mod_redirect'),
    url(r'^student/add/(?P<student_id>\d+)/$', 'student_add_redirect', name='student_add_redirect'),
)
