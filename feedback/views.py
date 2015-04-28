# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from pybursa.settings import ADMINS

from feedback.models import Letter


class LetterModelForm(forms.ModelForm):
	class Meta:
		model = Letter


class LetterCreateView(CreateView):
	model = Letter
	form_class = LetterModelForm
	success_url = reverse_lazy('feedback:letter') 
	
	def get_context_data (self, **kwargs):
		context = super(LetterCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u"Обратная связь"
		return context

	def form_valid(self, form):
		response = super(LetterCreateView, self).form_valid(form)
		send_mail(self.object.theme, self.object.body, self.object.email,
					[adress for (name, adress) in ADMINS], fail_silently=False)
		messages.success(self.request, u"Письмо успешно отправлено")
		return response
		