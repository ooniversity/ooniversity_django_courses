from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView


urlpatterns = [
    url(r'^$', views.FeedbackCreateView.as_view(), name='feedback_form'), 
]