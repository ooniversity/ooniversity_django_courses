# -*- coding: utf-8 -*-
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import mail_admins


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedbacks/feedback_form.html'

    def form_valid(self, form):
        response = super(FeedbackCreateView, self).form_valid(form)
        messages.success(self.request, u'Ваше письмо успешно отправлено!')
        mail_admins(self.object.theme, self.object.message, fail_silently=False)
        return response
