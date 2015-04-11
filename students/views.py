from django.shortcuts import render
from models import Student 

def students_list(request):
    course_id = request.GET.get('course_id')

    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(courses=course_id)
    return render(request, 'students_list.html', {'students': students})

def student_info(request, id):
    student = Student.objects.get(id=id)
    courses = student.courses.all()
    return render(request, 'student_detail.html', {'student': student, 'courses': courses})
