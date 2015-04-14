from django.contrib import admin
from courses.models import Courses, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [LessonInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('thema', 'text')

admin.site.register(Courses, CoursesAdmin)
admin.site.register(Lesson, LessonAdmin)
