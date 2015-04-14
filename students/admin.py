from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['name','surname', 'email', 'skype']
    list_filter = ['courset']
    fieldsets = [('Personal info', {'fields': ('name', 'surname', 'date_of_birth')}),
				 ('Contact info', {'fields': ('email', 'phone', 'address', 'skype')}),
				 (None, {'fields': ('courset',)})]
    filter_horizontal = ('courset',)



admin.site.register(Student, StudentAdmin)
