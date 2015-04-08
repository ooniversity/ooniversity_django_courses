from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'skype']
    search_fields = ['surname', 'email']
    list_filter = ['courses']
    fieldsets = (
        ('Personal info', {
           'fields': ('name', 'surname', 'birthday') 
        }),
        ('Contact info', {
            'fields': ('email', 'phone_num', 'address', 'skype', 'courses')
        }),
    )
    filter_horizontal = ('courses', )

admin.site.register(Student, StudentAdmin)
