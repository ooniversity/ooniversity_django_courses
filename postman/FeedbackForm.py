# coding=utf-8
from django import forms

from postman.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
