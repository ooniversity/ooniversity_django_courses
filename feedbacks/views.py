# -*- coding: UTF-8 -*-
from django.shortcuts import render,  redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django import forms
from django.core.mail import mail_admins
from django.contrib import messages
# from django.views.generic.create import CreateView
from django.views.generic import View
from models import Feedback


class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'


# class FeedbackCreateView(CreateView):
# 	model = Feedback
# 	template_name = "feedback_form.html"
# 	success_url = reverse_lazy('feedbacks:feedback_form')

# 	def get_context_data(self, **kwargs):
# 		context = super(FeedbackCreateView, self).get_context_data(**kwargs)
# 		context['page_title'] = u'Заполните контактную форму'
# 		context['button_value'] = u'Отправить'
# 		return context

# 	def form_valid(self, form):
# 		response = super(FeedbackCreateView, self).form_valid(form)
# 		mail_admins(subject=self.object.subject, 
# 			        message=self.object.text_message, 
# 			        fail_silently=False, 
# 			        connection=None, 
# 			        html_message=None)
# 		name = self.object.subject
# 		messages.info(self.request, u"Сообщение '%s' отправлено" % name)
# 		return response

class FeedbackView(View):
	form_class = FeedbackForm
	template_name = 'feedback_form.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form, 'page_title': u'Заполните контактную форму', 'button_value': u'Отправить'})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_feedback = form.save()
			mail_admins(subject=new_feedback.subject, 
			        message=new_feedback.text_message, 
			        fail_silently=False, 
			        connection=None, 
			        html_message=None)
			messages.success(request, u"Сообщение %s отправлено" % new_feedback.subject)
			return redirect('feedbacks:feedback_form')
		return render(request, self.template_name, 
        	{'form': form, 'page_title': u'Заполните контактную форму', 'button_value': u'Отправить'})	