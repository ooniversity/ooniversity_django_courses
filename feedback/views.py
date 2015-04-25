from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin

from feedback.models import Feedback, FeedbackForm
from django.conf import settings
from django.core.mail import send_mail

from django.views.generic.base import View


class FeedbackView(View):
    form_class = FeedbackForm
    template_name = "feedback/feedback.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            feedback = form.save()
            send_mail(feedback.subject, feedback.message, feedback.sender_email,
                      settings.ADMINS, fail_silently=False)
            messages.success(request, u"Message send success!")
            return redirect('feedback:feedbacks')

        return render(request, self.template_name, {'form': form})
