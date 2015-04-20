from django.contrib import admin
from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0

class LessonAdmin(admin.ModelAdmin):
	list_display = ['theme', 'num']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'about']
    list_display_links = ['title']
    search_fields = ['title']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
