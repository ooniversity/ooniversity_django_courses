from django.shortcuts import render
from models import Contact
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView


#  creating forms from models Student
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

# view for create student
class ContactFormView(FormView):
    form_class = ContactForm


    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание нового письма'
        return context

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 'Student %s %s successfully added'
                                       % (self.object.name, self.object.surname))
        return response
