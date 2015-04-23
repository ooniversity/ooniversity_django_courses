from django.contrib import admin
from mail.models import Mail

class MailAdmin(admin.ModelAdmin):
	list_display = ['email', 'mail_date']

admin.site.register(Mail, MailAdmin)
