from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'students.html')

def student_detail(request):
    return render(request, 'student_info.html')
