from django.contrib import admin
from django.db import models
from django.forms import widgets
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['your_email', 'date']


admin.site.register(Contact, ContactAdmin)
