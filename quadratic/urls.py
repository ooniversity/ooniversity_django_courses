from django.conf.urls import patterns, include, url
from quadratic import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^results/', 'quadratic.views.quadratic_results', name='results'),
)


