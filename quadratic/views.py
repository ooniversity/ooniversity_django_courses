# -*- coding: utf8 -*-
from django.shortcuts import render
from django import forms


class EquationForm(forms.Form):
	a = forms.IntegerField()
	b = forms.IntegerField()
	c = forms.IntegerField()

	def clean_a(self):
		data = self.cleaned_data['a']
		if data == 0:
			raise forms.ValidationError("коэффициент при первом слагаемом не может быть равным 0")
		return data

	
def quadratic_results(request):
	form = EquationForm(request.GET or None)
	if form.is_valid():
		a=form.cleaned_data["a"]
		roots, discr = get_roots(a=form.cleaned_data["a"],
        	                     b=form.cleaned_data["b"],
        	                     c=form.cleaned_data["c"])
		return render(request,'results.html', {'roots':roots, 'discr':discr, 'form':form, 'a':a})
	return render(request, 'results.html', {'form': form})


def get_discr(a,b,c):
	return b**2 - 4*a*c


def get_roots(a, b, c):
	roots = []
	discr = get_discr(a, b, c)
	if discr >= 0 and a != 0:
		roots = [(-b + discr**(1/2.0))/(2*a), (-b - discr**(1/2.0))/(2*a)]
	return roots, discr	

