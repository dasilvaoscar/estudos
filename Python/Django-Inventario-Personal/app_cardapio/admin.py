from django.contrib import admin    
from .models import *

@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    fields = ('nome','descricao', 'arquivo',)
    list_display = ('nome','descricao', 'arquivo', 'pub_date')
    list_filter = ('nome','descricao', 'arquivo', 'pub_date')
    search_fields = ('nome','descricao', 'arquivo', 'pub_date')