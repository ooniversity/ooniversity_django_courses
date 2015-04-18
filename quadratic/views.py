#coding: utf-8
from django import forms
from django.shortcuts import render
from quadratic import QuadraticEquation


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='Введите коэффециент a',
                           error_messages={'required': 'Это обязательное поле'})
    b = forms.IntegerField(label='Введите коэффециент b',
                           error_messages={'required': 'Это обязательное поле'})
    c = forms.IntegerField(label='Введите коэффециент c',
                           error_messages={'required': 'Это обязательное поле'})

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError("Коэффициент a не может быть равным нулю!")
        return a


def results(request):
    if request.GET == {}:
        form = QuadraticForm()
        c = {'form': form}
    else:
        form = QuadraticForm(request.GET)
        c = {'form': form}
        if form.is_valid():
            result = QuadraticEquation(**form.cleaned_data)
            result.solve()
            print type(result.d)
            c['result'] = result
    return render(request, 'result.html', c)
