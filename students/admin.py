from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'skype']
    search_fields = ['surname', 'email']
    list_filter = ['course']
admin.site.register(Student, StudentAdmin)
