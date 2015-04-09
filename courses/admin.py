from django.contrib import admin

from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    fk_name = "course"


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'descr_sm']
    search_fields = ['title']
    inlines = [LessonInline, ]
