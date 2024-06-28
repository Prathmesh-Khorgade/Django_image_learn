from django.contrib import admin
from.models import ImageModel

@admin.register(ImageModel)
class imageadmin(admin.ModelAdmin):
    list_display = ['id','name']
