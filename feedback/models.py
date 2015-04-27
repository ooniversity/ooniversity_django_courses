from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm, widgets


class Feedback(models.Model):
    sender_name = models.CharField("Your name", max_length=100)
    subject = models.CharField("Subject", max_length=300)
    sender_email = models.EmailField("Your email")
    message = models.TextField("Message", max_length=1000)
    create_at = models.DateTimeField(default=timezone.now, blank=True)


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        widgets = {
            'sender_email': forms.EmailInput,
            'create_at': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S')
        }
        exclude = ('create_at',)
        fields = '__all__'
