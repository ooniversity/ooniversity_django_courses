from django.contrib import admin

from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 3


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'short_description')
    search_fields = ['name']
    save_as = True


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
