# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from quadratic.models import *
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label=u"Коэффициент a:")
    b = forms.FloatField(label=u"Коэффициент b:")
    c = forms.FloatField(label=u"Коэффициент c:")

    def clean_a(a):
        a = a.cleaned_data['a']#'a'
        if float(a) == 0:
            raise forms.ValidationError(u"Коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return a

def parameters(request):
    context = {}
    errors = 0

    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')

            d = get_discr(a, b, c)
            context['d'] = d
            eq_root = get_eq_root(a, b, d)
            context['eq_root'] = eq_root               
        
    else:
        form = QuadraticForm()

    context['form'] = form         

    return render (request, 'results.html',context  )
