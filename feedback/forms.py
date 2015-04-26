from django.db import models
from django.forms import ModelForm, DateTimeField, DateTimeInput
import datetime
from django import forms
from feedback.models import Feedback

class FeedbackForm(ModelForm):
    date_created = DateTimeField(
        initial=datetime.datetime.now, 
        widget=DateTimeInput(attrs={'readonly':'readonly'})
    )
    class Meta:
        model = Feedback
        fields = '__all__'
