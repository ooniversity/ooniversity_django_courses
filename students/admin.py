from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info',{'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype', 'course']}),
    ]
    list_display = ('full_name', 'email', 'skype')
    search_fields = ['surname', 'email']
    list_filter = ['course']
    filter_horizontal = ('course',)

admin.site.register(Student, StudentAdmin)
