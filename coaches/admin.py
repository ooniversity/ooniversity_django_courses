from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    search_fields = ['user', 'email', 'description']
    list_display = ['user_full_name', 'description']
    list_filter = ['sex_choices']

    def user_full_name(self, obj):
        return unicode(obj.user.get_full_name())

admin.site.register(Coach, CoachAdmin)
