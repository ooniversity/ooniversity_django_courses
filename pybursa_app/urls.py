from django.conf.urls import patterns, include, url
from pybursa_app.views import StudentList, StudentListCourse, StudentDetail, StudentCreate
from pybursa_app.views import StudentEdit, StudentDelete, CourseDetail, CourseCreate


urlpatterns = patterns('pybursa_app.views',
    url(r'^$', 'index', name='index'),
    url(r'^course/(?P<pk>\d+)/$', CourseDetail.as_view(), name='course'),
    url(r'^course_add/$', CourseCreate.as_view(), name='course_add'),
    url(r'^coach/(?P<coach_id>\d+)/$', 'coach', name='coach'),

    url(r'^contacts/$', 'contacts', name='contacts'),
    url(r'^student_list/$', 'student_list', name='student_list'),
    url(r'^student_list/(\d+)/$', 'student_list', name='student_page'),
#    url(r'^student_list/$', StudentList.as_view(), name='student_list'),
    url(r'^student_list/(?P<course_id>\d+)/$', StudentListCourse.as_view(), name='student_cours'),
#    url(r'^student_list/(?P<course_id>\d+)/$', 'student_list', name='student_cours'),
#    url(r'^student_add/$', 'student_add', name='student_add'),
    url(r'^student_add/$', StudentCreate.as_view(), name='student_add'),
    url(r'^student_mod/(?P<pk>\d+)/$', StudentEdit.as_view(), name='student_mod'),
    url(r'^student_rem/(?P<pk>\d+)/$', StudentDelete.as_view(), name='student_rem'),
    url(r'^student_detail/(?P<pk>\d+)/$', StudentDetail.as_view(),name='student_detail'),
#    url(r'^student_detail/(?P<student_id>\d+)/$', 'student_detail',name='student_detail'),
    url(r'^student/mod/(?P<student_id>\d+)/$', 'student_mod_redirect', name='student_mod_redirect'),
    url(r'^student/add/(?P<student_id>\d+)/$', 'student_add_redirect', name='student_add_redirect'),
    url(r'^course/add/(?P<course_id>\d+)/$', 'course_add_redirect', name='course_add_redirect'),

)
