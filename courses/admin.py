from django.contrib import admin
from courses.models import Course, Lesson
# Register your models here.


class LessonInLine(admin.TabularInline):
    model = Lesson
    #field = ['theme', 'discription', 'number']
    item_display = ['theme', 'discription', 'number']


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'info']
    inlines = [LessonInLine]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
