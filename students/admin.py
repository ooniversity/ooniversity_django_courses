from django.contrib import admin
from students.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    list_display = ('full_name', 'email', 'scype', )

    def full_name(self, obj):
        return (obj.name + " " + obj.surname)

    filter_horizontal = ['courses']

    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'birth_date']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'scype']}),      
        (None, {'fields': ['courses']}),   
    ]

admin.site.register(Student, StudentAdmin)
