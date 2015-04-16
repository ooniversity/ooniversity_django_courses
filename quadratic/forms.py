#!/usr/bin/env python
# coding: utf-8

from django import forms


# Создание формы
class QuadraticForm(forms.Form):
    a = forms.IntegerField(label="коэфициент а")
    b = forms.IntegerField(label="коэфициент b")
    c = forms.IntegerField(label="коэфициент c")

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("Коэфициент при первом слагаемом"
                " уравнении не может быть равен нулю")
        return data
