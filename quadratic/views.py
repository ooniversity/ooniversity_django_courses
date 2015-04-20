from django.shortcuts import render, redirect
from django import forms


class QuadraticForm(forms.Form):
	a = forms.FloatField(label='Coefficient a ', required=True)
	b = forms.FloatField(label='Coefficient b ', required=True)
	c = forms.FloatField(label='Coefficient c ', required=True)

	def clean_a(self):
		data = self.cleaned_data['a']
		if data == 0:
			raise forms.ValidationError("Coefficient (a) can't be zero!")
		return data


def get_discr(a, b, c):
    d = b**2 - 4 * a * c
    return d


def get_eq_root(a, b, d, order=1):
    if order==1:
        x = (-b + d ** (1/2.0)) / 2 * a
    else:
        x = (-b - d ** (1/2.0)) / 2 * a
    return x


def quadratic_results(request):
	context = {'error': True}
	print request.POST
	if request.method == 'POST':
		form = QuadraticForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			context['a'] = data['a']
			context['b'] = data['b']
			context['c'] = data['c']
			a = context['a']
			b = context['b']
			c = context['c']
			d = get_discr(a, b, c)
			if d < 0:
				result_message = "D < 0, there are no real solutions"
			elif d == 0:
				x1 = get_eq_root(a, b, d)
				result_message = "D = 0, so only one root exists x1 = x2 = {}".format(x1)
			else:
				x1 = get_eq_root(a, b, d)
				x2 = get_eq_root(a, b, d, order=2)
				result_message = "Two roots exist: x1 = {} & x2 = {}".format(x1, x2)

			context.update({'d': d, 'result_message': result_message})
			context['error'] = False
	else:
		form = QuadraticForm()
	context['form'] = form
	return render(request, 'quadratic/index_q.html', context)