from django.db import models
from django.forms import ModelForm
from django import forms
from feedback.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
