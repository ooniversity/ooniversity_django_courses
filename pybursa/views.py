from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def mainP(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def stud_list(request):
	return render(request, 'student_list.html')

def stud_detail(request):
	return render(request, 'student_detail.html')
