from django import forms
from django.contrib.admin import widgets
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth' : widgets.AdminDateWidget()
        }
