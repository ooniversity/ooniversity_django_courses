# ~*~ coding: utf-8 ~*~

from django.contrib import admin

from courses.models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    fieldsets = [
        (None,                {'fields': ['lesson_number', 'lesson_theme']}),
        ('Содержание лекции', {'fields': ['lesson_description'], 'classes': ['collapse']}),
    ]
#    extra = 3



class CourseAdmin(admin.ModelAdmin):


    inlines = [LessonInline]
    extra = 3

class LessonAdmin(admin.ModelAdmin):
    fields = [('lesson_number', 'lesson_theme'), 'lesson_description']
    list_filter = ['lesson_course']
admin.site.register(Course,  CourseAdmin)
admin.site.register(Lesson, LessonAdmin)







