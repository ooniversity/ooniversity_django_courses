from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']
    search_fields = ['surname', 'email']

    fieldsets = [
        ('Pesonal Info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact Info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
    ]
    filter_horizontal = ['courses']

admin.site.register(Student, StudentAdmin)