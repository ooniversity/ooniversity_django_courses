from django.contrib import admin
from instructors.models import Instructor, Position, Course, Address
from django.db import models
from django.forms import widgets

# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
	list_display = ['name', 'surname', 'email', 'is_active']
	#fields = ['name', 'surname']
	#exclude = ['phone']
	list_display_links = ['name', 'email']
	list_max_show_all = 200
	list_per_page = 20
	actions_on_top = True
	actions_on_bottom = True
	date_hierarchy = 'date_of_birthday'
	ordering = ['surname', 'name']
	list_filter = ['is_active', 'position']
	search_fields = ['name','position__name']
	list_editable = ['is_active']

	readonly_fields = ['is_active']
	raw_id_fields = ['position']
	save_as = True
	save_on_top = True

	formfield_overrides = {
		models.DateField: { 'widget': widgets.TextInput}
		}

	fieldsets = [(None, {
							'fields': ['name', 'surname']
						}
				),
				('Extend information', {
										'fields': ['date_of_birthday','email','phone','slug', 'is_active', 'address', 'courses'],
										'classes': ['collapse']
										}
				)
				]

class InstructorInline(admin.StackedInline):
	model = Instructor
	fields = ['name', 'surname']

class PositionAdmin(admin.ModelAdmin):
	inlines = [InstructorInline]

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Course)
admin.site.register(Address)