from django.shortcuts import render
from coaches.models import Coach
from django.contrib.auth.models import User
from courses.models import Course
from datetime import *

def one_coach(request, pk):

    instructor = Coach.objects.filter(user_id=pk)[0]
    u_instructor = User.objects.get(coach=instructor)
    i_courses = Course.objects.filter(instructor_id=pk)
    a_courses = Course.objects.filter(assistant_id=pk)
    #assistant = Coach.objects.filter(user_id=pk)[0]
    #u_assistant = User.objects.get(coach=assistant)

    #print lessons
    #print lessons
    #newlessons = list(lessons)
    #print newlessons
    #print course
    #print course.id
    #course = qs.filter(id__in=(0,))
    #print 1
    #pub_date = date(2015, 04, 1)
    my_list = ['python', 'html', 'javascript']

    return render(request, "coach.html", {\
        'u_coach' : u_instructor, 'coach' : instructor, \
        'i_courses' : i_courses, 'a_courses' : a_courses, })# \
        #'my_list' : my_list })
        #, 'u_assistant' : u_assistant,
        #'instructor' : instructor })
        # 'assistant' : assistant, })

