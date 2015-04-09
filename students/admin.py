from django.contrib import admin
from students.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    search_fields = ['name', 'surname']
    list_display = ('fullname', 'email', 'scype', )
    filter_horizontal = ['courses']

    def fullname(self, obj):
        return (obj.name + " " + obj.surname)

admin.site.register(Student, StudentAdmin)
