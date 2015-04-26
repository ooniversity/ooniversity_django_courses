#!/usr/bin/python		
# -*- coding: UTF-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from django.views.generic import View
from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail, mail_admins

class FeedbackView(View):
    form_class = FeedbackForm 
    template_name = 'feedback/feedback.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        form = self.form_class()
        context['form'] = form
        context['form_title'] = u'Обратная связь'
        context['button_name'] = u'Отправить'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = dict()
        form = self.form_class(request.POST)
        context['form'] = form
        context['form_title'] = u'Обратная связь'
        context['button_name'] = u'Отправить'
        if form.is_valid():
            feedback = form.save()
            send_mail(feedback.topic, feedback.message, feedback.email,
                      settings.ADMINS, fail_silently=False)
            messages.success(request, 'Your message has been sent! Thank you!')
            return redirect('feedback:feedback')
        return render(request, self.template_name, context)
