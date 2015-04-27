# -*- coding: utf-8 -*-

from models import Contact
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse_lazy    # to clarify


#  creating forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        help_texts = {'name': u'Имя отправителя', 'subject': u'Тема письма', 'email': u'email отправителя'}
        fields = '__all__'


# first variant
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'feedbacks/contact_form.html'
    success_url = 'feedbacks:contact_form'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['page_title'] = u'Написать администратору сайта'
        return context

    def form_valid(self, form):
        #form = super(ContactFormView, self).form_valid(form)
        name = self.request.POST.get('name', '')
        subject = self.request.POST.get('subject', '')
        message = self.request.POST.get('body', '')
        from_email = self.request.POST.get('email', '')
        if name and subject and message and from_email:
            mail_admins(subject, message, fail_silently=True)
            messages.success(self.request, 'Mail successfully send')
            return HttpResponseRedirect('#')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')


# second variant
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'feedbacks/contact_form.html'
    form_class = ContactForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Написать администратору сайта'
        return context

    def form_valid(self, form):
        form = super(ContactCreateView, self).form_valid(form)
        name = self.object.name
        subject = self.object.subject
        message = self.object.body
        email = self.object.email
        date = self.object.date
        mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
        messages.success(self.request, 'Mail from %s successfully send' % name)
        return form

