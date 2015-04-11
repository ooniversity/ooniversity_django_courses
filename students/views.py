from django.shortcuts import render
from students.models import Student
from django.utils.datastructures import MultiValueDictKeyError

def student(request):
    try:
        crs_id = int(request.GET['course_id'])
        studs = Student.objects.filter(courses=crs_id)
        print studs
        print studs[0].courses
        return render(request, 'students/students.html', {'studik': studs})
    except MultiValueDictKeyError:
        studs = Student.objects.all()
        return render(request, 'students/students.html', {'studik': studs})
    

def get_student(request, s_id):
    stu = Student.objects.get(id=s_id)	
    
    return render(request, 'students/student.html', {'st':stu})
    
