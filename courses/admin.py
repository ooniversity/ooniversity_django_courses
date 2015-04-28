from django.contrib import admin

from courses.models import Course, Lesson


class LessonAdmin(admin.ModelAdmin):
	exclude = ['course']


class LessonInLine(admin.TabularInline):
	model = Lesson
	extra = 0
	

class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'short_description', 'id']
	search_fields = ['title']
	inlines = [LessonInLine]	

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
