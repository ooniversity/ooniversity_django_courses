# -*- coding: utf-8 -*-
from django.shortcuts import render
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import mail_admins


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = "/feedback"
    template_name = 'feedbacks/feedback_form.html'

    def form_valid(self, form):
        response = super(FeedbackCreateView, self).form_valid(form)
        messages.success(self.request, u'Ваше письмо успешно отправлено!')
        data = form.cleaned_data
        mail_admins(data['theme'], data['message'], fail_silently=False)
        # mail_admins(form.theme, form.message, form.sender_email, ['to@example.com'], fail_silently=False)
        return response
