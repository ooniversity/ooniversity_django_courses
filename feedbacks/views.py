# -*- coding: UTF-8 -*-

from pybursa import settings
from django import forms
from feedbacks.models import Feedback
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView

class FeedbackCreateView(CreateView):
    model = Feedback
    template_name ='feedbacks/feedback_form.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, u'Форма %s отправлена' %instance.name)
        admin_list = [admin_email for admin_name, admin_email in settings.ADMINS]
        send_mail(instance.subject, instance.message, instance.email,
                  admin_list, fail_silently=False)

        return super(FeedbackCreateView, self).form_valid(form)

