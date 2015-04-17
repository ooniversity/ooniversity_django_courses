import datetime

from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from courses.models import Course
from django import forms
from django.forms import widgets


class Student(models.Model):
    name = models.CharField("Name", max_length=25)
    surname = models.CharField("Surname", max_length=25)
    birthday = models.DateField("Birthday")
    email = models.EmailField("Email", unique=True)
    phone_num = models.CharField(
        verbose_name=u'Phone number',
        unique=True, max_length=12)
    address = models.CharField(
        "Address", max_length=256)
    skype = models.CharField("Skype", max_length=128)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name

    def get_courses(self):
        return "\n".join([p.title for p in self.courses.all()])

    @property
    def all_courses(self):
        return self.courses.all()

    @property
    def full_name(self):
        return self.name + " " + self.surname


class StudentForm(ModelForm):
    class Meta:
        model = Student
        widgets = {
            'email': forms.EmailInput,
            'courses': forms.SelectMultiple,
        }
        labels = {
            'phone_num': 'Phone',
        }

    def clean_name(self):
       name = self.cleaned_data['name'].capitalize()
       return name

    def clean_surname(self):
       surname = self.cleaned_data['surname'].capitalize()
       return surname