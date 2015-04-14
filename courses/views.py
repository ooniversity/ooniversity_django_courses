from django.shortcuts import render_to_response
from courses.models import Course
from coaches.models import Coach

def course_view(request):
    model = Course.objects.all()
    return render_to_response('index.html', {'model': model})

def course_plan(request, pk):
    planmodel = Course.objects.get(pk=pk)
    lessons = planmodel.coursekey.all().order_by('order_number')
    course = Course.objects.all().filter(id=pk)[0]
    coach = Coach.objects.all().filter(user=course.coach.user)
    assistant = Coach.objects.all().filter(user=course.assistant.user)
    return render_to_response('courses.html', {
        'planmodel': planmodel,
        'lessons': lessons,
        'coach': [coach[0], coach[0].descr],
        'assistant': [assistant[0], assistant[0].descr],
        })