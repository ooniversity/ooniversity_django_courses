# -*- coding: utf-8 -*-

from django import forms
from feedback.models import FeedbackMessage


class FeedbackMessageForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = '__all__'


