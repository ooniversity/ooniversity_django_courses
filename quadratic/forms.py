# -*- coding: utf-8 -*-

from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label="Коэффициент a")
    b = forms.IntegerField(label="Коэффициент b")
    c = forms.IntegerField(label="Коэффициент c")

    def __init__(self, *args, **kwargs):
        super(QuadraticForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} не задан!'.format(
                fieldname=field.label)}

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("Коэффициент при первом слагаемом не может быть равен нулю!")
        return data
