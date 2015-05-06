from django.contrib import admin
from  courses.models import  Course, Lesson




    

class LessonInLine(admin.TabularInline):
    model = Lesson
    field = ['consecutive_number', 'theme', 'discription']
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'short_description']
    search_fields = ['course_title']


    inlines = [LessonInLine]
    save_on_top = True


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
