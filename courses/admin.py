from django.contrib import admin
from django.db import models
from django.forms import widgets
from courses.models import Course, Lesson


admin.site.register(Course)
admin.site.register(Lesson)
