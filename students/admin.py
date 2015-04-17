from django.contrib import admin
from django.forms import widgets
from students.models import Student


def upper_case_name(obj):
    # title() - in case when name/surname
    return ("%s %s" % (obj.name, obj.surname)).title()
upper_case_name.short_description = 'Full name'				 # start with small letters


class StudentAdmin(admin.ModelAdmin):
    list_display = [upper_case_name, 'email', 'skype']
    list_display_links = [upper_case_name]
    search_fields = ['surname', 'email']
    list_filter = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']}),
    ]
    filter_horizontal = ['courses']

admin.site.register(Student, StudentAdmin)
