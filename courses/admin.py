# -*- coding: utf-8 -*-
from django.contrib import admin
from courses.models import Course, Lesson, Comment
# Register your models here.


class LessonInLine(admin.TabularInline):
    model = Lesson
    #field = ['theme', 'discription', 'number']
    item_display = ['theme', 'discription', 'number']


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'info']
    inlines = [LessonInLine]

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['autor']
    list_display = ['autor', 'course', 'date_public']
    list_filter = ['course', 'date_public']

admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Lesson)
