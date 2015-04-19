from django.contrib import admin
from students.models import Student 

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'email', 'skype']
    list_filter = ['course']
    filter_horizontal = ['course']
    fieldsets = [
        ('Personal info',{'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'adress', 'skype', 'course']}),
    ]


"""class StudentAddAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'email', 'skype']
    list_filter = ['course']
    filter_horizontal = ['course']
    fieldsets = [
        ('Personal info',{'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'adress', 'skype', 'course']}),
    ]"""
admin.site.register(Student, StudentAdmin)
"""admin.site.register(StudentAdd,StudentAddAdmin)"""


