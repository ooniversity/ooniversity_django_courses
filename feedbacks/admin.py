from django.contrib import admin
from feedbacks.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    search_fields = ['email', 'date']
    #list_filter = ['courses']
    #fieldsets = [('Personal info', {'fields': ('name', 'surname', 'date_of_birth')}),
				# ('Contact info', {'fields': ('email', 'phone', 'address', 'skype')}),
				 #(None, {'fields': ('courses',)})]
    #filter_horizontal = ('courses',)


admin.site.register(Contact, ContactAdmin)