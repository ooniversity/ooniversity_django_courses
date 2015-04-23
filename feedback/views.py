from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from feedback.models import Feedback, FeedbackForm

from django.views.generic.base import View


class FeedbackView(View):
    form_class = FeedbackForm
    initial = {'key': 'value'}
    template_name = "feedback/feedback.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            feedback = form.save()
            messages.success(request, u"Message send success!")
            return HttpResponseRedirect('/feedback/')

        return render(request, self.template_name, {'form': form})
