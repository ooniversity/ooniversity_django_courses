from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Info',{'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact Info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
    ]
    
    list_display = ['full_name', 'email', 'skype']
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    filter_horizontal = ['courses']
    
    def full_name(self, obj):
        return "%s %s" % (obj.name, obj.surname)
   
    

admin.site.register(Student, StudentAdmin)


