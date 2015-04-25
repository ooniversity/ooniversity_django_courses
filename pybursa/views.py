import datetime

from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm, DateTimeField, DateTimeInput
from django.contrib import messages

from django.core.mail import send_mail

from courses.models import Course
from coaches.models import Coach
from feedbacks.models import Feedback

from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView, BaseCreateView, ModelFormMixin, FormMixin
from django.views.generic.detail import SingleObjectMixin, SingleObjectTemplateResponseMixin

from pybursa.settings import ADMINS

class FeedbackAddForm(ModelForm):
    date_of_create = DateTimeField(initial=datetime.datetime.now, widget=DateTimeInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Feedback
        fields = '__all__'


class HomeView(generic.ListView):
    template_name = 'index.html'
    model = Course


def contact(request):
    coaches = Coach.objects.all()
    return render(request, 'contact.html', {'coaches': coaches})


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')


class FeedbackView(SingleObjectTemplateResponseMixin, TemplateResponseMixin, BaseCreateView, ModelFormMixin, FormMixin, SingleObjectMixin, ProcessFormView, View):
    form_class = FeedbackAddForm
    template_name = 'feedback.html'
    model = Feedback

    def form_valid(self, form):
        response = super(FeedbackView, self).form_valid(form)
        messages.info(self.request, 'Message was sent! The message was sent at {}.'.format(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")))
        send_mail(self.object.name, 'Theme: {}\n\n{}'.format(self.object.theme, self.object.body), self.object.email, [email for admin, email in ADMINS], fail_silently=False)
        return response
