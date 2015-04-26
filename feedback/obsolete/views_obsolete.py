#!/usr/bin/python		
# -*- coding: UTF-8 -*-
from django.conf import settings
#from django.template import Context
from django.shortcuts import render, redirect
from feedback.models import Feedback, FeedbackForm
from django.views.generic import View
from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail, mail_admins

class FeedbackForm(forms.ModelForm):#obsolete
    class Meta:
        model = Feedback    

#https://gist.github.com/Skycker/10557009
#http://www.pydanny.com/simple-django-email-form-using-cbv.html
def feedback(request):#obsolete
    form_title = u'Обратная связь'
    button_name = u'Отправить'
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            #date = form.cleaned_data['date']
            #data = form.cleaned_data
            #send_mail(data['topic'], data['message'], data['email'],
            #          ['olena.persianova@gmail.com'], fail_silently=False )
            """
            send_mail(topic, 
                      message, 
                      email, 
                      ['olena.persianova@gmail.com'],
                      fail_silently=False )
            """
            """
            send_mail(topic, 
                      message, 
                      email, 
                      settings.ADMINS,
                      fail_silently=False )
            """
            mail_admins(topic, 
                      message, 
                      connection=None,
                      html_message=None)
            Feedback.objects.create(name=name, topic=topic,
                                    message=message, 
                                    email=email)
            messages.success(request, 'Your message has been sent! Thank you!')
            return redirect('feedback:feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', 
            {'form': form, 'form_title': form_title, 
            'button_name': button_name
        })
