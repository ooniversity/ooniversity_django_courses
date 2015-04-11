from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['surname', 'email', 'skype']
#    list_display = ['my_url_field', 'email', 'skype']
#    def my_url_field(self, obj):
#        return '<a href="%s%s">%s</a>' % ('surname', obj.url_field, obj.url_field)
#    my_url_field.allow_tags = True
#    my_url_field.short_description = 'Full name'
#    raw_id_fields = ['']
    list_filter = ['courses']
admin.site.register(Student, StudentAdmin)
