from django.contrib import admin
from coaches.models import Coach
from courses.models import Course
from django.contrib.auth.models import User




#class CoachInline(User.StackedInline):
#    model = Coach

#class ExtendedUserAdmin(UserAdmin):
#    inlines = UserAdmin.inlines + (CoachInline,)

#admin.site.unregister(User)
#admin.site.register(User, ExtendedUserAdmin)





#class UserInline(admin.TabularInline):
#    model = User
#    extra = 0


class Course_instructrorInline(admin.TabularInline):
    verbose_name = "Course"
    verbose_name_plural = "Instructor"
    fk_name = 'instructor'
    model = Course
    extra = 2

class Course_assistantInline(admin.TabularInline):
    verbose_name = "Course"
    verbose_name_plural = "Assistant"
    fk_name = 'assistant'
    model = Course
    extra = 2


class CoachAdmin(admin.ModelAdmin):

    model = Coach
    #filter_vertical = ('courses',)
    #search_fields = ['title']
#    list_display = [ 'user', 'gender']


    search_fields = ['user']
    list_display = [ 'user', 'skype', 'phone']
    list_filter = ['user']
    #filter_vertical = ['user']
    inlines = [Course_instructrorInline, Course_assistantInline]


#    list_editable = ['title']
#admin.site.register(Course, CourseAdmin)


admin.site.register(Coach, CoachAdmin)

# Register your models here.



#class CoachInlines(admin.StackedInline):
#    model = Coach

#class CoachAdmin(admin.ModelAdmin):
#    inlines = [CoachInlines]

#    def queryset(self, request):
#        qs = super(CoachAdmin, self).queryset(request)
#        qs = qs.exclude(relatedNameForYourProduct__isnone=True)
#        return qs

#admin.site.register(CoachProxy, CoachAdmin)
