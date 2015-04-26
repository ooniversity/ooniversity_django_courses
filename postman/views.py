# coding=utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

#from django.conf import settings
from django.core.mail import mail_admins

from FeedbackForm import FeedbackForm


class FeedbackView(TemplateView):
    template_name = "postman/feedback.html"
    success_message = u"Ваше сообщение успешно отправлено"
    action_name = u"Отправить"

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        context['action_name'] = self.action_name
        return context

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            mail_admins(subject, body)
            messages.success(request, self.success_message)
            form = FeedbackForm()
        #return HttpResponse('Hello, World!')
        #return redirect('feedback')
        return render(request, self.template_name, {
            'form': form,
            'action_name': self.action_name,})

