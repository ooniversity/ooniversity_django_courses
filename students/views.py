from django.shortcuts import render_to_response
from django.views import generic
from .models import Student

class StudentListView(generic.ListView):
	model = Student
	context_object_name = 'students'

class StudentDetailView(generic.DetailView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		
		#average score
		#obj = super(StudentDetailView, self).get_object()
		#completed_tasks = obj.completedtask_set.all()
		#tasks_count = completed_tasks.count()
		#total_score = sum([task.score for task in completed_tasks])
		#av_score = total_score/tasks_count if tasks_count > 0 else 0
		#context['av_score'] = av_score

		#rating
		return context

def  dummy_render(request, pk=0, template="students/student_list.html"):
	return render_to_response(template)
