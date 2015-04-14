from django.shortcuts import render
from django.views import generic

from students.models import Student
from courses.models import Course


class StudentsView(generic.ListView):
    template_name = 'students/students.html'
    model = Student

    def get_queryset(self):
        query = Course.objects.filter(id=self.request.GET.get('course_id'))
        if query:
            return Student.objects.filter(course=query)
        else:
            return Student.objects.all()


class StudentView(generic.ListView):
    template_name = 'students/student.html'
    model = Student

    def get_queryset(self):
        qs = super(StudentView, self).get_queryset().filter(id=self.kwargs['id'])
        return qs
