# -*- coding: utf-8 -*-
from django import forms
from models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        labels = {'sender_name': "Имя",
                  'sender_email': "E-mail",
                  'theme': "Тема",
                  'message': "Сообщение",
                  }
        exclude = ['date_create']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Поле {fieldname} обязательно должно быть заполнено!'.format(
                fieldname=field.label)}
