from django.conf.urls import patterns, url
#from students.views import  edit_student, delete_student
from students import views


urlpatterns = patterns('',
url(r'^students/$', views.StudentListView.as_view(), name = 'student-list'),
url(r'^students/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name = 'student-info'),
# URLs for edition students
url(r'^students/add/$', views.StudentCreateView.as_view(), name='student-add'),
url(r'^students/edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='student-edit'),
url(r'^students/remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='student-del'),
)