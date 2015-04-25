# -*- coding: utf_8 -*-
from django.core.mail import mail_admins, send_mail, send_mass_mail
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from feedback.models import Feedback


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = u'Сообщение с темой "%(subject)s" было отправлено'

    def form_valid(self, form):
        from_email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message'] + u'\n\nСообщение от ' + name + u'\n' + from_email
        mail_admins(subject, message)
        return super(FeedbackCreateView, self).form_valid(form)