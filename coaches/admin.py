from django.contrib import admin
from  coaches.models import  Coach, User


class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone', 'skype']
    search_fields = ['phone', 'skype']
    list_filter = ['gender']
admin.site.register(Coach, CoachAdmin)
admin.site.register(User)

