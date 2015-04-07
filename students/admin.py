from django.contrib import admin
from django.db import models
from django.forms import widgets
from students.models import Student


admin.site.register(Student)
