# -*- coding: utf-8 -*-

from django import forms

from students.models import Student


# Create form for model Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = '__all__'
