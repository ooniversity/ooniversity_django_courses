from django.contrib import admin
from  courses.models import  Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'short_description']
    search_fields = ['course_title']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
