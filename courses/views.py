from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

#from polls.models import Choice, Question

def index(request):
    courses = Course.objects.all()
    return render(request, "index.html", {'courses' : courses})


def detail(request, pk):
    course = Course.objects.filter(id=pk)[0]
    lessons = Lesson.objects.filter(course=pk)
    instructor = Coach.objects.filter(user_id=course.instructor_id)[0]
    u_instructor = User.objects.get(coach=instructor)
    assistant = Coach.objects.filter(user_id=course.assistant_id)[0]
    u_assistant = User.objects.get(coach=assistant)

    #print lessons
    #print lessons
    #newlessons = list(lessons)
    #print newlessons
    #print course
    #print course.id
    #course = qs.filter(id__in=(0,))
    return render(request, "courses/detail.html", {'course' : course, 'lessons' : lessons,\
        'u_instructor' : u_instructor, 'u_assistant' : u_assistant,\
        'instructor' : instructor, 'assistant' : assistant, })

#class DetailView(generic.DetailView):
#    model = Course
#    template_name = 'courses/detail.html'


#def dj101_contact(request):
#    return render(request, "contact.html")

#def dj101_student_list(request):
#    return render(request, "student_list.html")

#def dj101_student_detail(request):
#    return render(request, "student_detail.html")



#def vote(request, question_id):
#    p = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': p,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

