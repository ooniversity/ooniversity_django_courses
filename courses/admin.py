from django.contrib import admin
from django.db import models
from django.forms import widgets

from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ['theme', 'description', 'number']
    extra = 0

class LessonAdmin(admin.ModelAdmin):
    list_display = ['topic', 'description']

class LessonInline(admin.StackedInline):
    model = Lesson
    #fields = ['name']

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'short_description']
    list_display = ['name', 'short_description']
    inlines = [LessonInline]



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)





