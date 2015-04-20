from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django import forms
from django.contrib import messages

def courses_home_page(request):
	courses = Course.objects.all()
	return render(request, 'courses.html', {'courses': courses})

def courses_one_of(request, pk):
	course_one = Course.objects.get(id=pk) #id?
	lessons = course_one.lessons.all()
	trainer = Coach.objects.all().filter(user=course_one.trainer.user)[0]
	assistant = Coach.objects.all().filter(user=course_one.assistant.user)[0]
	return render(request, 'oneofcourse.html', 
		{'course':course_one, 
		'lessons':lessons,
		'trainer':trainer, 
		'assistant':assistant,
		})

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course

class LessonForm(forms.ModelForm):
	class Meta:
		model = Lesson

def add_course(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
		 	application = form.save()

		 	messages.success(request, 'Course saved!')

		 	return redirect('courses:add')

	else:
		form = CourseForm()
	return render(request, 'add.html',{'form':form})
	

def edit_course(request, pk):
	course = Course.objects.get(id=pk)

	if request.method == 'POST':
		form = CourseForm(request.POST, instance=course)
		if form.is_valid():
			application = form.save()
		 	messages.success(request, 'Course saved! [by edit]')

		 	#return redirect('course:index')
	else:
		form = CourseForm(instance=course)
	return render(request, 'edit.html', {'form':form})
	
def delete_course(request, pk):
	course = Course.objects.get(id=pk)

	if request.method == 'POST':
		course.delete()
		messages.success(request, 'Object deleted!')
	 	return redirect('courses:index')
	return render(request, 'delete.html',{'course':course})

def add_lesson(request, pk):
	if request.method == 'POST':
		form = LessonForm(request.POST)
		if form.is_valid():
		 	application = form.save()

		 	messages.success(request, 'Lesson saved!')

		 	return redirect('courses:index')

	else:
		form = LessonForm()
	return render(request, 'add_lesson.html',{'form':form})
