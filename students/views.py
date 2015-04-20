from students.models import Student, CourseApplication
from courses.models import Course, Lesson
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib import messages


class CourseApplicationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['slug']
        labels = {'email': "Mail"}
        help_texts = {'email': 'Enter Personal email'}

def stud_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", 
                 {'students': students})

def detail(request, student_id):
    crs = Student.objects.get(id=student_id)
    return render(request, 'students/student_detail.html',
                 {'a': crs, 'lesson': Student.objects.all().filter(courses=student_id)})

def registred(request):
    return render(request, "students/registy_completed.html")

def apply_to_course(request):
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, "User added!")
            return redirect('/students/registred/')
    else:
        form = CourseApplicationForm()
    return render(request, "students/apply.html", {'form': form})

def edit_from_course(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, "User saved!")
            return redirect('/students/registred/')
    else:
        form = CourseApplicationForm()   
    form = CourseApplicationForm(instance=application)
    return render(request, "students/edit.html", {'form': form})

def delete_from_course(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
        application.delete()
        messages.success(request, "User Removed!")
        return redirect('/students/registred/')
    return render(request, "students/delete.html", {'application': application})
