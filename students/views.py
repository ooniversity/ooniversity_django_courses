from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django import forms

class StudentApplyForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	package = forms.ChoiceField(choices=(
									('standart','Standart'),
									('premium','Premium'),
									('gold','Gold')
								),
								widget = forms.RadioSelect)
	subscribe = forms.BooleanField(required=False)

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

	return render(request, "students.html", {'students':students})


def one_of_student(request, pk):
	#http://127.0.0.1:8000/students/1/
	student = Student.objects.get(pk=pk)
	return render(request, 'oneofstudent.html', {'student':student})

def apply_to_course(request):
	print request.POST, request.method

	if request.method == 'POST':
		form = StudentApplyForm(request.POST)
		if form.is_valid():

			print "----------------  Do something!"
			print form.cleaned_data
			print "\n"
			print form.cleaned_data['subscribe']

			return redirect('/')
	else:
		form = StudentApplyForm()	
	return render(request, 'apply.html', {'form':form})



