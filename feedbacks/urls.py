from django.conf.urls import url
from . import views
from django.views.generic import View


urlpatterns = [
    url(r'^$', views.FeedbackView.as_view(), name='feedback_form'), 
]