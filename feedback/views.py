# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic.edit import CreateView

from pybursa.settings import ADMINS

from feedback.models import Feedback


class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = '#'

    def form_valid(self, form):
        response = super(FeedbackCreateView, self).form_valid(form)
        messages.success(self.request, u'Сообщение отправлено!')
        send_mail(self.object.subject, self.object.message, self.object.senders_email,
                  [k for i, k in ADMINS], fail_silently=False)
        return response
