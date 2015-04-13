from django.contrib import admin

from students.models import Student


# configuration class for model Student
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'birth_date']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']}),
    ]
admin.site.register(Student, StudentAdmin)
