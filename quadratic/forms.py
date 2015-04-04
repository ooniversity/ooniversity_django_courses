from django import forms

class QuadraticForm(forms.Form):
	a = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'aria-describedby': 'basic-addon1'}))
	b = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'aria-describedby': 'basic-addon1'}))
	c = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'aria-describedby': 'basic-addon1'}))