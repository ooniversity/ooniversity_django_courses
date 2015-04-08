from django.contrib import admin
from django.db import models
from django.forms import widgets
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    list_display_links = ['name']
    search_fields = ['name']
    inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
