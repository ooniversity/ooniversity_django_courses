# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMessage
from django.views.generic.edit import FormView, View
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django import forms
from models import Contact
from django.core.mail import mail_admins


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "contact/feedback.html"
    success_url = '/feedback/'

    def form_valid(self, form):
        try:
            message = "\n\n{0}".format(form.cleaned_data.get('body'))
            subject = form.cleaned_data.get('subject').strip()
            mail_admins(subject, message, fail_silently=False)
            form.save()
            messages.success(self.request, u'Спасибо! Ваше сообщение отправлено')
            return super(ContactFormView, self).form_valid(form)
        except Exception as e:
            print e, "EXC"
