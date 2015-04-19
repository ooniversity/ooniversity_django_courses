from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django import forms
from django.contrib import messages

#class StudentApplyForm(forms.Form):
#	name = forms.CharField(max_length=50)
#	email = forms.EmailField()
#	package = forms.ChoiceField(choices=(
#									('standart','Standart'),
#									('premium','Premium'),
#									('gold','Gold')
#								),
#								widget = forms.RadioSelect, initial = 'standart')
#	subscribe = forms.BooleanField(required=False)
#
#class CourseForm(forms.ModelForm):
#	class Meta:
#		model = Course
#		#fields = ['name', 'short_description']
#		#exclude = ['description']
#		#widget = {'package': forms.RadioSelect}
#		labels = {'name':'!name'}
#		help_texts = {'name': "Enter NAME!!!"}

def students_all(request):
	#http://127.0.0.1:8000/students/
	#http://127.0.0.1:8000/students/?course_id=1

	#print request.GET.get('course_id')
	
	cid = request.GET.get('course_id')

	if cid == None:
		students = Student.objects.all()
	else:
		#course = Course.objects.get(pk=int(cid))
		#students = course.students.all()
		students = Course.objects.get(pk=int(cid)).students.all()
		#!!!!!!! CORRECT = students = Students.objects.filter(courses__id=course_id)

	return render(request, "students.html", {'students':students})


def one_of_student(request, pk):
	#http://127.0.0.1:8000/students/1/
	student = Student.objects.get(pk=pk)
	return render(request, 'oneofstudent.html', {'student':student})

#def apply_to_course(request):
#	if request.method == 'POST':
#		form = CourseForm(request.POST)
#		if form.is_valid():
#			data = form.cleaned_data
#			app = Course()
#			name = models.CharField(max_length=255)
#	else:
#		form = CourseForm()	
#	return render(request, 'apply.html', {'form':form})

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student

def add_student(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
		 	application = form.save()

		 	messages.success(request, 'Student saved!')

		 	return redirect('students:add')

	else:
		form = StudentForm()
	return render(request, 'add.html',{'form':form})

def edit_student(request, pk):
	student = Student.objects.get(id=pk)

	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			application = form.save()
		 	messages.success(request, 'Student saved! [by edit]')

		 	#return redirect('students:index')
	else:
		form = StudentForm(instance=student)
	return render(request, 'edit.html', {'form':form})

def delete_student(request, pk):
	student = Student.objects.get(id=pk)

	if request.method == 'POST':
		student.delete()
		messages.success(request, 'Object deleted!')
	 	return redirect('students:index')
	return render(request, 'delete.html')

