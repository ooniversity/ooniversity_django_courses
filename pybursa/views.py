from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student 
from coaches.models import Coach
from datetime import datetime

def show_index(request):
	courses = Course.objects.all()
	return render(request, 'index.html', {'courses': courses})

def contacts(request):
	return render(request, 'contacts.html', {'date_now': datetime.now()})

def show_students(request):
    if request.GET.get('course_id') is None:
        students = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': students})
    else:
        students = Student.objects.filter(courses__id = int(request.GET.get('course_id')))
        return render(request, 'students/student_list.html', {'students': students})

def show_student(request, id):
    student = Student.objects.get(id = int(id))
    return render(request, 'students/student_detail.html', {'student': student})

def show_course(request, id):
    course = Course.objects.get(id = int(id))
    lessons = Lesson.objects.filter(course__name = course.name)
    return render(request, 'courses/course.html', {'course': course, 'lessons': lessons})

def show_coach(request, id):
    coach = Coach.objects.get(id = int(id))
    courses = Course.objects.all()
    teacher = []
    assistant = []
    for i in courses:
        if coach.user == i.teacher.user:
            teacher.append(i)
    for i in courses:
        if coach.user == i.assistant.user:
            assistant.append(i)
    return render(request, 'coaches/coach.html', {'coach': coach, 'teacher': teacher, 'assistant': assistant})