from django import forms
from feedbacks.models import MessageFeedback


class MessageFeedbackForm(forms.ModelForm):
    class Meta:
        model = MessageFeedback



