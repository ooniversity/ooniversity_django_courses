from django.shortcuts import render
from django.views import generic

from students.models import Student


class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Student.objects.order_by('-id')[:5]

def linked_students(request):
    #p = get_object_or_404(Course, pk=course_id)
    course = Course.objects.get(id=pk)
    linked_students = Student.objects.filter(course=pk)
    return render(request, 'students/index.html', {'course': course, 'lesson_list': linked_students})

def student_detail(request):
    pass
