from django.contrib import admin

from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'descr_sm']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['theme', 'num_in_plan', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)