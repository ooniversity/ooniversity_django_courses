from django.contrib import admin
from students.models import Student


def full_name(obj):
	return ("%s %s" % (obj.name, obj.surname))

full_name.short_description = 'Full name'

 
class StudentAdmin(admin.ModelAdmin):
	list_display = [full_name, 'email', 'skype']	
	search_fields = ['surname', 'email']
	list_filter = ['courses']	
	fieldsets = [('Personal info', {'fields': ['name', 'surname', 'birth_date']}),
	             ('Contact info', {'fields':['email', 'phone', 'adress', 'skype']}),
	             (None, {'fields': ['courses']})]
	filter_horizontal = ['courses']

admin.site.register(Student, StudentAdmin)
