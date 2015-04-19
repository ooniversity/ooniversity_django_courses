from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django.contrib import messages
from django import forms

class CourseAddForm(forms.ModelForm):
	class Meta:
		model = Course

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('item_no')
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

def add_course(request):
	if request.method == 'POST':
		form = CourseAddForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'Course is added')
			return redirect('index')
	else:
		form = CourseAddForm()
	return render(request, 'courses/add.html', {'form': form})


def edit_course(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseAddForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'Course info is updated')
			return redirect('index')
	else:
		form = CourseAddForm(instance=application)
	return render(request, 'courses/edit_course.html', {'form': form})


def delete_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
        print request.POST
        application.delete()
        messages.success(request, 'Course info been deleted')
        return redirect('index') 
    return render(request, 'courses/delete_course.html')