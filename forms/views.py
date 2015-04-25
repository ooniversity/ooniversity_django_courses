# -*- coding: UTF-8 -*-

from django import forms
from forms.models import Feedback
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView

class FeedbackCreateView(CreateView):
    model = Feedback
    template_name ='forms/feedback_form.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, u'Форма %s отправлена' %(instance.name))
        return super(FeedbackCreateView, self).form_valid(form)

