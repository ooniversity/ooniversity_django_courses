from django.contrib import admin
from students.models import Student
from courses.models import Course


#class CourseInline(admin.TabularInline):
#    model = Course
#    extra = 1

class StudentAdmin(admin.ModelAdmin):
#    model = Course
    filter_horizontal = ('courses',)
    fieldsets = (
        ('Personal info', {
            'fields': ('surname', 'name', 'date_of_birth')
        }),
        ('Contact info', {
            'fields': ('email', 'phone', 'addr', 'skype', 'courses')
        }),
    )
    #fields = (('surname','name'))
    search_fields = ['surname', 'email']
    list_display = ['full_name', 'email', 'skype']
#    model = Course
#    filter_horizontal = ('courses',)
#    inlines = [CourseInline,]

#    list_display = ['my_url_field', 'email', 'skype']
#    def my_url_field(self, obj):
#        return '<a href="%s%s">%s</a>' % ('surname', obj.url_field, obj.url_field)
#    my_url_field.allow_tags = True
#    my_url_field.short_description = 'Full name'
#    raw_id_fields = ['']
    list_filter = ['courses']

admin.site.register(Student, StudentAdmin)
