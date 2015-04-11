from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from courses.models import Course, Lesson


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.order_by('-id')[:5]

def lesson_detail(request, pk):
    course = Course.objects.get(id=pk)
    lesson_list = Lesson.objects.filter(course=pk)
    return render(request, 'courses/detail.html', {
                'course': course,
                'lesson_list': lesson_list,
    })

"""
class DetailView(generic.DetailView):
    template_name = 'courses/detail.html'
    model = Course

    context_object_name = 'lesson_list'

    def get_queryset(self):
        return Lesson.objects.filter(course=pk)

"""


