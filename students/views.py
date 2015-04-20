from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course 
from django import forms
from django.contrib import messages

class StudentAddForm(forms.ModelForm):
	class Meta:
		model = Student



def students(request):
    course_id = request.GET.get('course_id')
    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(course=course_id)
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = student.course.all()
    return render(request, 'students/student_detail.html', {'student': student, 'courses': courses})

def add_student(request):
	if request.method == 'POST':
		form = StudentAddForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'Student is added')
			return redirect('students:students')
	else:
		form = StudentAddForm()
	return render(request, 'students/add.html', {'form': form})


def edit_student(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentAddForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'Student info is updated')
			return redirect('students:students')
	else:
		form = StudentAddForm(instance=application)
	return render(request, 'students/edit_student.html', {'form': form})


def delete_student(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
        print request.POST
        application.delete()
        messages.success(request, 'Student info been deleted')
        return redirect('students:students') 
    return render(request, 'students/delete_student.html')

	
    
    
