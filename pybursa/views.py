from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from students.models import Student
from courses.models import Course, Lesson
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwards):
        context = super(TemplateView, self).get_context_data(**kwards)
        context['courses'] = Course.objects.all()
        return context


