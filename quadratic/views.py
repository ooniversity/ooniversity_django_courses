# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='a  ')
    b = forms.IntegerField(label='b  ')
    c = forms.IntegerField(label='c  ')

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("Koeffitsient pri pervom slagaemom uravneniya ne mozhet byit ravnyim nulyu")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data


"""
class Coefficient(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.erroe_message = None

    def is_valid (self):
        if not self.value:
            self.error_massage = "Koeffitsient ne opredelen"
            return False

        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_message = "Koeffitsient ne tseloe chislo"
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_massage = "Koeffitsient pri pervom slagaemom uravneniya ne mozhet byit ravnyim nulyu"
"""




def quadratic(request):
    form = QuadraticForm()
    return render(request, 'quadratic.html', {'form':form})

def result(request):
    print "\n"
    print request
    print "\n"
    print request.method
    print "\n"
    d_status = ''
    d = 0
    
    if request.META['QUERY_STRING'] == "":
        form = QuadraticForm()
    elif request.method == 'GET':
        form = QuadraticForm(request.GET)
        if form.is_valid():
            print "-=-=-=-=-=- URA_GET!\n"
            print form.cleaned_data
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
     

            d = float(b*b   - 4*a*c)

            if d > 0:
                x1 = float((-b + d**0.5) / 2*a)
                x2 = float((-b - d**0.5) / 2*a)
                d_status = "Kvadratnoe uravnenie imeet 2 deystvitelnyih kornya: x1 = %s, x2 = %s" % (x1,x2)
            elif d == 0:
                x1 = x2 = float(- b / 2*a)
                d_status = "Diskriminant raven nulyu, kvadratnoe uravnenie imeet odin deystvitelnyiy koren: x1 = x2 = %s" % x1
            else:
                d_status = "Diskriminant menshe nulya, kvadratnoe uravnenie ne imeet deystvitelnyih korney"


    return render(request, 'results.html', { 'd':[d, d_status], 'form':form}  )