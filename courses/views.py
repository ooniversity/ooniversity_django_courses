from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from courses.models import Course, Lesson


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-id')

def detail(request, pk):
    course = Course.objects.get(id=pk)
    lesson_list = Lesson.objects.filter(course=pk)
    return render(request, 'courses/detail.html', {'course': course, 'lesson_list': lesson_list})

def contact(request):
    return render(request, 'courses/contact.html')



