from django.conf.urls import patterns, url

from students import views


urlpatterns = patterns('',
    url(r'^$', views.ItemListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='detail'),
    url(r'^add/', views.ItemCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.ItemUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.ItemDeleteView.as_view(), name='remove'),
)
