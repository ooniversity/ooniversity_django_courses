from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ['user']

admin.site.register(Student, StudentAdmin)
