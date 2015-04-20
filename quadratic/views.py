#!/user/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django import forms

from quadratic.models import ReportAnError, ResultsCalc
from quadratic.utils import QuadraticEquation

class QuadraticForm(forms.Form):
    a = forms.FloatField(label=u"коэффициент a")
    b = forms.FloatField(label=u"коэффициент b")
    c = forms.FloatField(label=u"коэффициент c")

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError(u"коэффициент при первом слогаемом уравнения не может быть равным нулю")
        return data


def quadratic_results(request):
    context = {}

    if request.GET:
        form = QuadraticForm(request.GET)

        if form.is_valid():
            a = float(form.cleaned_data.get('a'))
            b = float(form.cleaned_data.get('b'))
            c = float(form.cleaned_data.get('c'))

            qe = QuadraticEquation(a, b, c)
            qe.calc_discr()
            discriminant = qe.get_discr()

            context['line_1'] = "%s" %ResultsCalc.objects.get(id=1)
            context['discriminant'] =  discriminant   

            if discriminant < 0:
                context['line_2'] = "%s" %ResultsCalc.objects.get(id=2)
            else:
                x1 = qe.get_eq_root()
                x2 = qe.get_eq_root(order = 2)

                if x1 == x2:
                    context['line_2'] = "%s x1 = x2 = %g" %(ResultsCalc.objects.get(id=3), x1)
                else:
                    context['line_2'] = "%s x1 = %d  x2 = %d" %(ResultsCalc.objects.get(id=4), x1, x2)
    else:
        form = QuadraticForm()
    context['form'] = form
    return render(request, "result.html", context)

