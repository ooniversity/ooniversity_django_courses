# -*- coding: utf-8 -*-

from django.contrib import messages
from django.conf import settings
from django.core.mail import mail_admins
from django.views.generic.edit import CreateView
from feedback.models import FeedbackMessage
from feedback.forms import FeedbackMessageForm


class FeedbackMessageCreateView(CreateView):
    model = FeedbackMessage
    template_name = 'feedback.html'
    form_class = FeedbackMessageForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(
            FeedbackMessageCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(FeedbackMessageCreateView, self).form_valid(form)
        email_message = u'Отправитель: ' + self.object.mailer + u'\n'
        email_message += u'E-mail: ' + \
            self.object.resp_email + u'\n'
        email_message += u'Дата отправки: ' + \
            unicode(self.object.date) + u'\n'
        mail_admins(self.object.theme, email_message, fail_silently=True)

        date = self.object.date
        messages.success(self.request,
                         u'Ваш отзыв "{0}" отправлен администраторам в {1}:{2}'
                         .format(self.object.theme, date.hour, date.minute))
        return form
