# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(required=True, label='коээфициент a:')
    b = forms.IntegerField(required=True, label='коээфициент b:')
    c = forms.IntegerField(required=True, label='коээфициент c:')

    def clean_a(self):
        a_data = self.cleaned_data['a']
        if a_data == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю.")
        return a_data

def quadratic_results(request):
    form = QuadraticForm()
    data = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            discr = data['b'] ** 2 - 4 * data['a'] * data['c']
            print discr
            x1 = 0
            x2 = 0
            if discr == 0:
                x1 = x2 = -float(data['b']) / 2 * data['a']
            elif discr > 0:
                x1 = float(-data['b'] + discr ** 0.5) / (2 * data['a'])
                x2 = float(-data['b'] - discr ** 0.5) / (2 * data['a'])
            data['x1'] = x1
            data['x2'] = x2
            data['discr'] = discr
            data['form'] = form
    context = {'data': data, 'form': form}
    return render(request, 'quadratic.html', context)
