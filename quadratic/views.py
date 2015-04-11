# coding: utf8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict

def quadratic_results(request):

	errors = {'a': '', 'b': '', 'c': ''}

	variables = {'a': str(request.GET['a']), 'b': str(request.GET['b']), \
					'c': str(request.GET['c'])} 
	discr = None
	x1 = None
	x2 = None


	if variables['a'] == '0':
		errors['a'] = 'коэффициент при первом слогаемом уравнении не может быть равен нулю'

	for var in variables:
		if variables[var] == '':
			errors[var] = 'коэффициент не определен'
			continue
		try: 
			variables[var] = int(variables[var])
		except ValueError:
			errors[var] = 'коэффициент не целое число'

	temp = ''.join(errors.values()) 

	if temp == '': #if errors are empty == a,b,c are valid

		discr = variables['b']**2 - 4*variables['a']*variables['c']
		if discr >= 0:
			x1 = (-variables['b'] - discr**0.5) / 2*variables['a']
			x2 = (-variables['b'] + discr**0.5) / 2*variables['a']


	return render(request, 'quadratic_results.html', \
		{'variables': variables, 'errors': errors, 'discr': discr, \
			'x1': x1, 'x2': x2})