from django.contrib import admin
from courses.models import Course, Lesson

class LessonInLine(admin.TabularInline):
    model = Lesson
    item_display = ['theme', 'discription', 'number']

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'brief']
    inlines = [LessonInLine]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
