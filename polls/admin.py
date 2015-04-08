from django.contrib import admin
from polls.models import Choice, Question
from courses.models import Course, Lesson
from students.models import Student

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'description']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)