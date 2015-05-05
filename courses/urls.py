from django.conf.urls import patterns, url


from courses.views import add_lesson


from courses.views import CourseDetailView


from courses.views import CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = patterns('',
    url(r'^courses/(?P<id_course>\d+)/$', CourseDetailView.as_view(), name='course-coaches'),
    # URLs for edition courses with using Class-Based-Views
    url(r'^courses/add/$', CourseCreateView.as_view(), name='add-course'),
    url(r'^courses/edit/(?P<pk_course>\d+)/$', CourseUpdateView.as_view(), name='edit-course'),
    url(r'^courses/remove/(?P<pk_course>\d+)/$', CourseDeleteView.as_view(), name='del-course'),
    # URLs for edition lessons
    url(r'^courses/(?P<pk_course>\d+)/add_lesson/$', add_lesson, name='add-lesson'),
)