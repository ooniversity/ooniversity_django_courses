from django.shortcuts import render, redirect,
from feedbacks.models import Feedback
from django import forms

class FeedbackAppForm(forms.ModelForm):
    class Meta:
        model = Feedback
    


    def add_feedback(request):
    if request.method == 'POST':
        feedback_form = FeedbackAppForm(request.POST)
        if feedback_form.is_valid():
            data = feedback_form.cleaned_data
            send_mail(data['theme'], data['message'], data['email'], 
                            ['khazar65@mail.ru'], fail_silently=False)
            messages.success(request, 'Собщение отправлено')
            return redirect('feedbacks:feedback')
    else:
        feedback_form = FeedbackAppForm()
    return render(request, 'feedbacks/add_feedback.html', {'feedback_form': feedback_form})