# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import QuadraticForm
from .utils import quadratic_solver

def quadratic(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = QuadraticForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			answer = quadratic_solver(a, b, c)
			return render(request, 'quadratic/index.html', {'form': form, 'answer': answer})

	# if a GET (or any other method) we'll create a blank form
	elif request.method == 'GET':
		if request.GET.get('a','') or request.GET.get('b','') or request.GET.get('c',''):
			form = QuadraticForm(request.GET)
			if form.is_valid():
				a = form.cleaned_data['a']
				b = form.cleaned_data['b']
				c = form.cleaned_data['c']
				answer = quadratic_solver(a, b, c)
				return render(request, 'quadratic/index.html', {'form': form, 'answer': answer})
		else:
			form = QuadraticForm()
			return render(request, 'quadratic/index.html', {'form': form})

	return render(request, 'quadratic/index.html', {'form': form})
