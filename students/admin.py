# ~*~ coding: utf-8 ~*~

from django.contrib import admin


from students.models import Student
from courses.models import Course, Lesson
#class CourseInline(admin.StackedInline):
#    model = Course
#    fieldsets = [
#        (None,                {'fields': ['course_name', 'course_brief']}),
#        ('Содержание курса', {'fields': ['course_description'], 'classes': ['collapse']}),
#    ]

class StudentAdmin(admin.ModelAdmin):

    list_display = ("student_last_name","student_name", "student_addr")
    list_filter = ['student_course']
#    inlines = [CourseInline]
#    filter_vertical= ["student_course"]
    raw_id_fields = ("student_course",)
admin.site.register(Student, StudentAdmin)

