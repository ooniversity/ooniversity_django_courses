from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact/contact.html')


def student_list(request):
    return render(request, 'student_list/student_list  .html')


def student_detail(request):
    return render(request, 'student_detail/student_detail.html')
