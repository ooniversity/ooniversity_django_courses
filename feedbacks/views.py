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
        send_message = 'Message from Name:{0},E-mail:{1} \n\n {2} \n Send at {3}'.format(
            self.object.sender_name, self.object.sender_email, self.object.message,
            self.object.date_create.strftime("%d.%m.%Y %H:%M:%S")
        )
        messages.success(self.request, u'Ваше письмо успешно отправлено!')
        mail_admins(self.object.theme, send_message, fail_silently=False)
        return response
