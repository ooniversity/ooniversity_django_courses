from django.contrib import admin

from feedback.models import Letter


class LetterAdmin(admin.ModelAdmin):
	list_display = ['email', 'send_time']
	readonly_fields = ['send_time']	

admin.site.register(Letter, LetterAdmin)