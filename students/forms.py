# -*- coding: utf-8 -*-
from django import forms
from students.models import Student
# Create form for model Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student