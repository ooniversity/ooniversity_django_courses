#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label="коэффициент a")
    b = forms.FloatField(label="коэффициент b")
    c = forms.FloatField(label="коэффициент c")

    def clean_a(self):
    #https://docs.djangoproject.com/en/1.7/ref/forms/validation/#cleaning-a-specific-field-attribute
        a=self.cleaned_data['a']
        if a==0:
            raise forms.ValidationError("коеффициент при первом слагаемом уравнения не может быть равен нулю")
        return a

def quadratic(request):
    return render(request, 'quadratic/quadratic.html')

def results(request):
    context = dict()
    if request.GET:
    #if request.method == "GET":
        #context = dict()
        form = QuadraticForm(request.GET)
        message=''
        discriminant=0
        if form.is_valid():
            a = float(form.cleaned_data.get('a', ''))
            b = float(form.cleaned_data.get('b', ''))
            c = float(form.cleaned_data.get('c', ''))            
            discriminant=int(b**2-4*a*c)
            context['discriminant']=discriminant
            if discriminant<0:
                message='Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif discriminant==0:
                x=round(float(-b/(2.0*a)), 2)
                message='Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
            else:
                x1=round(float((-b+(b**2-4*a*c)**0.5)/2.0*a), 2)
                x2=round(float((-b-(b**2-4*a*c)**0.5)/2.0*a), 2)
                message='Квадратное уравнение имеет два действительных корня: х1 = %s , x2 = %s' % (x1, x2)
        context['message']=message
    else:
        form = QuadraticForm()
    context['form']=form
    return render(request, 'quadratic/results.html', context)

