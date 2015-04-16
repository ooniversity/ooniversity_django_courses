#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, redirect
from django import forms

from .forms import QuadraticForm


def quadratic_results(request):

    discr = None
    x1 = None
    x2 = None

    if request.GET:
        # проинстанцировали форму
        form = QuadraticForm(request.GET)
        
        if form.is_valid():
            data = form.cleaned_data
            a, b, c = data['a'], data['b'], data['c']

            discr = b ** 2 - 4 * a * c

            if discr == 0:
                x1 = x2 = float(-b) / 2 * a
            elif discr > 0:
                x1 = float(-b + discr ** 0.5) / (2 * a)
                x2 = float(-b - discr ** 0.5) / (2 * a)
    else:
        form = QuadraticForm()
    
    return render(request, 'quadratic_results.html', {
        'x1': x1,
        'x2': x2,
        'discr': discr,
        # передача формы в шаблон
        'form': form,
    })
