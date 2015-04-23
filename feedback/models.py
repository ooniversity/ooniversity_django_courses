from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm, widgets


class Feedback(models.Model):
    name_sender = models.CharField("Sender name", max_length=100)
    subject = models.CharField("Theme of message", max_length=300)
    message = models.TextField("Message", max_length=1000)
    email_sender = models.EmailField("Sender email")
    date_create = models.DateTimeField(default=timezone.now, blank=True)


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        widgets = {
            'email': forms.EmailInput,
            'message': forms.TextInput,
            'date_create': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S')
        }
        exclude = ('date_create',)
        fields = '__all__'
