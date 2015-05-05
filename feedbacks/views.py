# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from django.contrib import messages
from django.views.generic.edit import CreateView

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackModelForm


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackModelForm
    success_url = reverse_lazy('feedbacks:feedback-form')

    def form_valid(self, form):
        self.feedback = form.save()

        # Формирование письма для отправки
        subject = self.feedback.mail_theme	# u'Пагинация - есть хорошо!'	# unicode(self.feedback.mail_theme)
        message_mail = u'Письмо от: {},  E-mail: {}\n\nОтправлено: {}\n\n---\n\n{}\n'.format(
            self.feedback.sender_name, self.feedback.sender_email,
            self.feedback.mail_datetime.strftime('%Y-%m-%d  %H:%M'),
            self.feedback.mail_body
        )
        mail_admins(subject, message_mail, fail_silently=False)

        # Формирование сообщения об успешной отправке письма
        message = u'Ваше письмо от {}, E-mail: {} на тему {} успешно отправлено !!!'.format(
            self.feedback.sender_name, self.feedback.sender_email, subject
        )
        messages.success(self.request, message)
        return super(FeedbackCreateView, self).form_valid(form)

