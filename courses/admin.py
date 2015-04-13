from django.contrib import admin

# Register your models here.

from courses.models import Course, Lesson


class LessonInLine(admin.TabularInline):
    model = Lesson
    field = ['number', 'theme', 'discription']
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'short_descript']

    inlines = [LessonInLine]

    #ordering = ['title']

    save_on_top = True


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
