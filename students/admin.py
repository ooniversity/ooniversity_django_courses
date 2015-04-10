from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	
    list_display = ('full_name', 'email', 'skype')
    search_fields = ['surname', 'email']
    filter_horizontal = ('courses', )
    list_filter = ['courses']

    fieldsets = (
		('Personal info', {'fields': ('name', 'surname', 'birth_date')}), 
		('Contact info', {'fields': ('email', 'phone', 'address', 'skype', 'courses')}),
		)


admin.site.register(Student, StudentAdmin)
