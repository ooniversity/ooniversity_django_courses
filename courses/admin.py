from django.contrib import admin
from courses.models import Course, Lessons


class LessonsInline(admin.TabularInline):
	model = Lessons
	fields = ['theme', 'description', 'number']	


class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	search_fields = ['name']
	inlines = [LessonsInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lessons)
