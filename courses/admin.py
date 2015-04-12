from django.contrib import admin
from courses.models import Course, Lesson



class LessonAdmin(admin.ModelAdmin):
    list_display = ['theme','description', 'order_number']



class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0



class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','short_description']
    inlines = [LessonInline]
    search_fields = ['name']



    

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)

