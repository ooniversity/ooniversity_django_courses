from django.shortcuts import render

def course_info(request):
    return render (request, 'index.html')

def contact_list(request):
    return render (request, 'contact.html')

def student_list(request):
    return render (request, 'student_list.html')

def student_detail(request):
    return render (request, 'student_detail.html')
