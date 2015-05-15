from django.contrib import admin
from news.models import New
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text']
    list_display = ['title', 'date_public', 'likes', 'dislikes']
    list_filter = ['date_public']


admin.site.register(New, NewAdmin)
