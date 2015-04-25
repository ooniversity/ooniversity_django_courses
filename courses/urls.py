from django.conf.urls import patterns, url

from courses import views
from courses import views_lesson


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='detail'),
    url(r'^add/', views.ItemCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.ItemUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.ItemDeleteView.as_view(), name='remove'),
    # lessons
    url(r'^(?P<pk>\d+)/add_lesson/', views_lesson.item_add, name='add_lesson'),
)
