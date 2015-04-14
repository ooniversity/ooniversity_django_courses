from django.contrib import admin
from students.models import Students

class StudentsAdmin(admin.ModelAdmin):
	list_display = [ 'f_name', 'email', 'skype' ]
	search_fields = [ 'surname', 'email' ]
	list_filter = [ 'course' ]
	
	fieldsets = [
		('Personal Info', {'fields': ('first_name', 'surname', 'birdth_date')}),
        ('Contact Info', {'fields': ('email', 'phone', 'adress', 'skype')}),
        (None, {'fields': ('course', )}),
        ]
	filter_horizontal = ('course',)

admin.site.register(Students, StudentsAdmin)
