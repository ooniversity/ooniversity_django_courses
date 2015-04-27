from django.contrib import admin
from django import forms
from django.db import models
from pybursa_emails.models import Mail

class MailAdmin(admin.ModelAdmin):
    list_display =('sender_email', 'message_date')

#    fields = [('sender_email', 'message_date')]
    list_filter = ['message_date']

admin.site.register(Mail, MailAdmin)
