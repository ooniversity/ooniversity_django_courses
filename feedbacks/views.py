# -*- coding: utf-8 -*-


from django.shortcuts import render
from models import Contact
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView


#  creating forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        help_texts = {'name': u'Имя отправителя', 'subject': u'Тема письма', 'email': u'email отправителя'}
        fields = '__all__'

        def send_email(self):
        # send email using the self.cleaned_data dictionary
            data = form.cleaned_data
            data.send_email()


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'feedbacks/contact_form.html'
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание письма'
        return context

    def form_valid(self, form):
        form.send_email()
        #message = u'Письмо отправлено'
        #messages.success(self.request, message)
        return super(ContactFormView, self).form_valid(self, form)
