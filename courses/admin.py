from django.contrib import admin
from courses.models import Course, Lesson


admin.site.register(Lesson)

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'descr']
    list_editable = ['title']
admin.site.register(Course, CourseAdmin)
