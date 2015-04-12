from django.contrib import admin

from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'comment')
    inlines = [
        LessonInline,
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)

