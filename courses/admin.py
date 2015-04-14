from django.contrib import admin
from courses.models import Course, Lesson

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'description', 'index' )

#class LessonInline(admin.StackedInline):
class LessonInline(admin.TabularInline):
    model = Lesson
    #fields = ['topic']
    extra = 0
    #ordering = ['index']

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'short_description', )
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)


