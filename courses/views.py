from django.shortcuts import get_object_or_404, render
from django.views import generic

from courses.models import Course


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Course.objects.all()


def course_detail(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    course_lesson_list = c.lesson_set.all()
    template_name = 'courses/detail_course.html'
    return render(request, template_name, {'course': c,
                                           'course_lesson_list': course_lesson_list,
                                           })
