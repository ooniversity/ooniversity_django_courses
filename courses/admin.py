from django.contrib import admin

from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    fk_name = "course"

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'descr_sm']
    search_fields = ['title']
    inlines = [LessonInline,]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['theme', 'num_in_plan', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)