from django.shortcuts import render
from contactwithemail.models import emailmodel
from django.views.generic.edit import DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from django import forms
from django.forms import ModelForm
from django.contrib import messages
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, redirect

class ContactWithEmailForm(forms.ModelForm):
    class Meta:
       model = emailmodel

#class EmailCreateView(CreateView):
#    model = emailmodel
#    template_name = 'contactwithemail/emailmodel.html'
#    success_url = reverse_lazy('contactwithemail:success.html')
#
 #   def get_context_data(self, **kwargs):
 #       context = super(EmailCreateView, self).get_context_data(**kwargs)
 #       context['page_title'] = 'Send Email'
 

def send_feedback(request):
    if request.method == 'POST':
        form = ContactWithEmailForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u"Email sent")
            return redirect('feedback:feedback')
    else:
        form = ContactWithEmailForm()
    return render(request, "contactwithemail/sendemail.html", {'form': form})

