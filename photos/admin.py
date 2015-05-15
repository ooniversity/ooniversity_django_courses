from django.contrib import admin
from photos.models import Photo

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['discription']


admin.site.register(Photo, PhotoAdmin)
