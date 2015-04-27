# -*- coding: utf-8 -*-

from django import forms

from feedbacks.models import Feedback


# Create form for model Student

class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback

        fields = '__all__'
