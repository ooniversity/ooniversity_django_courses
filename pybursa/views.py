from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class StudentListView(TemplateView):
    template_name = 'student_list.html'

class StudentDetailView(TemplateView):
    template_name = 'student_detail.html'

