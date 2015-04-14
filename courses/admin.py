from django.contrib import admin
from courses.models import Course, Lesson

class LessonAdmin(admin.ModelAdmin):
	list_display = ['theme', 'number', 'course']

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)