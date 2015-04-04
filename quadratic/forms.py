# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):
	a = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'aria-describedby': 'basic-addon1'}))
	b = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'aria-describedby': 'basic-addon1'}))
	c = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'aria-describedby': 'basic-addon1'}))

	def clean_a(self):
		a = self.cleaned_data['a']
		if a == 0:
			raise forms.ValidationError('Не может быть равным нулю')
		return a