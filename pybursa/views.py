from django.shortcuts import render
from django.http import HttpResponse

def show_index(request):
	return render(request, 'index.html')

def contacts(request):
	return render(request, 'contacts.html')

def students(request):
	return render(request, 'students.html')

def student_1(request):
	return render(request, 'student_1.html')