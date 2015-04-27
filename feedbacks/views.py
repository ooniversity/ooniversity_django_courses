# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from feedbacks.models import MessageFeedback
from feedbacks.forms import MessageFeedbackForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic.edit import CreateView
from django.views.generic.base import View



class MessageFeedbackCreateView(CreateView):
    model = MessageFeedback
    template_name = 'feedbacks/feedback.html'
    form_class = MessageFeedbackForm
    success_url = '#'


    def form_valid(self, form):
        response = super(MessageFeedbackCreateView, self).form_valid(form)
        messages.success(self.request, u'Ваше сообщение успешно отправлено!')
        mail_admins(self.object.theme, self.object.message, fail_silently=False)
        return response
    



