from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display = ['fullname', 'mail', 'skype']
	search_fields = ['surname', 'mail']
	list_filter = ['courses']
	filter_horizontal = ('courses',)
	fieldsets = [('Personal info', {'fields': ('name', 'surname', 'date_birthday')}),
				 ('Contact info', {'fields': ('mail', 'phone', 'address', 'skype')}),
				 (None, {'fields': ('courses',)})
				 ]
	

admin.site.register(Student, StudentAdmin)