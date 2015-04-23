from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        super_valid = super(StudentCreateView, self).form_valid(form)
        msg = "Student {} {} was added!".format(self.object.name, self.object.surname)
        messages.success(self.request, msg)
        return super_valid


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        msg = "Student edited!"
        messages.success(self.request, msg)
        return super(StudentUpdateView, self).form_valid(form) 


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def delete(self, request, *args, **kwargs):
        delete_super = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request,
                         u'Student {} deleted.'.format(self.object.name))
        return delete_super


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        courseid = self.request.GET.get('course_id', None)
        if courseid is None:
            students = Student.objects.all()
        else:
            students = Student.objects.filter(courses__id = courseid)
        return students


class StudentDetailView(DetailView):
    model = Student