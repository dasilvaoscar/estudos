from django.contrib import admin
from .models import Setor, Telefone


class AdminTelefone(admin.ModelAdmin):
    exclude = ()
    list_display = ('nome', 'ramal', 'email', 'setor')
    list_display_links = ('nome', 'ramal', 'email', 'setor')
    search_fields = ('nome', 'ramal', 'email', 'setor')


admin.site.register(Telefone, AdminTelefone)
admin.site.register(Setor)