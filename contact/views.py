# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            mail_admins(data['subject'], data['body'], fail_silently=False)
            messages.success(request, "Messages was sent")
            return redirect('contact/feedback')
    else:
        form = ContactForm()
    return render(request, 'contact/feedback.html', {'form': form})
