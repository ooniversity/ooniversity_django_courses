from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):

    list_display = ('user', 'user_name', 'scype', 'user_email',)
    list_filter = ['gender']
    search_fields = ['user__first_name', 'user__last_name', 'scype']

    fieldsets = [
        ('Pesonal Info', {'fields': ['user', 'gender', 'birth_date',]}),
        ('Contact Info', {'fields': ['phone', 'address', 'scype',]}),
        (None, {'fields': ['description']})
    ]

#http://stackoverflow.com/questions/24569687/searching-by-related-fields-in-django-admin

admin.site.register(Coach, CoachAdmin)
