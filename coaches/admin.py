from django.contrib import admin

from  coaches.models import  Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'full_name', 'user_email', 'date_of_birth', 'gender', 'skype']  
    search_fields = ['phone', 'skype', 'user__username', 'user__email', 'user__first_name', 'user__last_name',]
    list_filter = ['gender']
    
admin.site.register(Coach, CoachAdmin)


