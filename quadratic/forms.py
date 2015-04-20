# -*- coding: utf-8 -*-

from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label="коэффициент a", required=True)
    b = forms.FloatField(label="коэффициент b", required=True)
    c = forms.FloatField(label="коэффициент c", required=True)


    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError('коэффициент при первом слогаемом уравнения не может быть равным нулю')
        else:
            return data


