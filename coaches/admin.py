from django.contrib import admin

# Register your models here.

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'full_name', 'user_email',
                    'date_of_birth', 'gender', 'skype']

    list_filter  = ['gender']

    search_fields = [
        'skype', 'phone', 'address',
        'user__username', 'user__email',
        'user__first_name', 'user__last_name',
    ]


admin.site.register(Coach, CoachAdmin)
