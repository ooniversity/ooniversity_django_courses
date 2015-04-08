from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pesonal Info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact Info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['course']})
    ]
    filter_horizontal = ['course']

    list_display = ('full_name', 'email', 'skype')
    list_filter = ['course']
    search_fields = ['surname', 'email']

    def full_name(self, obj):
        return ("%s %s" % (obj.name, obj.surname)).upper()

    full_name.short_description = 'Full name'

admin.site.register(Student, StudentAdmin)
