from django.contrib import admin
from students.models import Student 

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['fullname', 'email', 'skype']
    list_filter = ['courses']
    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'birthday']}),
    ('Contact info', {'fields': ['email', 'cell', 'address', 'skype',]}),
    (None, {'fields': ['courses']})]
    filter_horizontal = ['courses']

admin.site.register(Student, StudentAdmin)


