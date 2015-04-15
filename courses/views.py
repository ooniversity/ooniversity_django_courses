from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def course_detail(request, course_id):
    try:
        course_current = Course.objects.get(id=int(course_id))
        course_name = course_current.name
        course_description = course_current.description
        student_id = str(course_id)
        lessons = Lesson.objects.filter(course = course_current)

        trainer_info = {
            "id": course_current.trainer.id,       
            "fullname": course_current.trainer.user.get_full_name(),
            "description": course_current.trainer.description,
            #"url": "coaches/"+str(course_current.trainer.id)+"/"
        }

        assistant_info = {
            "id": course_current.assistant.id,       
            "fullname": course_current.assistant.user.get_full_name(),
            "description": course_current.assistant.description,
            #"url": "coaches/"+str(course_current.assistant.id)+"/"
        }
 
        message = ""
        return render(request, 'courses/course_detail.html', {"lessons": lessons, "message": message, "student_id": student_id, "course_name": course_name, "course_description": course_description, 'trainer_info': trainer_info, 'assistant_info': assistant_info})
    except ObjectDoesNotExist:
        message = "Sorry, no course with id = %s exists yet."%(course_id)
        return render(request, 'course_detail.html', {"message": message})
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.get
