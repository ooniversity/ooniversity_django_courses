from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django import forms
from django.forms.extras.widgets import SelectDateWidget

from static.python.AdminImageWidget import AdminImageWidget
from students.models import Student
from courses.models import Course


birth_years = xrange(2015,1930,-1)


class StudentAddForm(forms.ModelForm):
    
    class Meta:
        model = Student
        widgets = {'course': forms.CheckboxSelectMultiple(), 'date_of_birth': SelectDateWidget(years=birth_years), 'image': AdminImageWidget()}
        labels = {'image': 'Photo'}
        help_texts = {'course': "You can choose more then one course." , 'image': 'Not a required field.', 'address': 'Not a required field.'}
        fields = '__all__'



class StudentsView(generic.ListView):
    template_name = 'students/students.html'
    model = Student

    def get_queryset(self):
        query = Course.objects.filter(pk=self.request.GET.get('course_id'))
        if query:
            return Student.objects.filter(course=query)
        else:
            return Student.objects.all()


class StudentView(generic.ListView):
    template_name = 'students/student.html'
    model = Student

    def get_queryset(self):
        qs = super(StudentView, self).get_queryset().filter(pk=self.kwargs['pk'])
        return qs

def student_add(request):
    context = dict()
    if request.method == 'POST':
        form = StudentAddForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Registration complite!')
            return redirect('students')
    else:
        form = StudentAddForm()
    context['form'] = form
    return render(request, 'students/add_student.html', context)

def student_edit(request, pk):
    application = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentAddForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Changes have been saved!')
    else:
        form = StudentAddForm(instance=application)
    return render(request, 'students/edit_student.html', {'form': form})

def student_remove(request, pk):
    application = Student.objects.get(pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.warning(request, u'Object {} {} deleted!'.format(application.surname, application.name))
        return redirect('students')
    return render(request, 'students/delete_student.html', {'application': application})