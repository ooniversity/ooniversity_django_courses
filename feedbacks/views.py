# -*- coding: UTF-8 -*-
from django.shortcuts import render,  redirect
from django.core.urlresolvers import reverse_lazy
from django import forms
from django.core.mail import mail_admins
from django.contrib import messages
from django.views.generic.edit import CreateView
from models import Feedback


class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'


class FeedbackCreateView(CreateView):
	model = Feedback
	template_name = "feedback_form.html"
	success_url = reverse_lazy('feedbacks:feedback_form')

	def get_context_data(self, **kwargs):
		context = super(FeedbackCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Заполните контактную форму'
		context['button_value'] = u'Отправить'
		return context

	def form_valid(self, form):
		response = super(FeedbackCreateView, self).form_valid(form)
		mail_admins(subject=self.object.subject, 
			        message=self.object.text_message, 
			        fail_silently=False, 
			        connection=None, 
			        html_message=None)
		name = self.object.subject
		messages.info(self.request, u"Сообщение '%s' отправлено" % name)
		return response
