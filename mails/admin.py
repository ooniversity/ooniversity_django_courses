from django.contrib import admin
from mails.models import Mail

class MailAdmin(admin.ModelAdmin):
    list_display = ['address_sender', 'mail_date']


admin.site.register(Mail, MailAdmin)
