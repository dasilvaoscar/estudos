from django.contrib import admin
from .models import Licenca, Custo


class LicencaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome']}),
        ('Atribuição de Usuário', {'fields': ['usuario']}),
        ('Valores', {'fields': ['valor_unitario']}),
    ]
    list_display = ('nome', 'get_licenca_usuario', 'valor_unitario', 'Quantidade',)
    list_display_links = ('nome', 'get_licenca_usuario', 'valor_unitario', 'Quantidade')
    search_fields = ['nome', 'usuario', 'valor_unitario']
    list_filter = ('nome', 'usuario', 'valor_unitario',)
    filter_horizontal = ['usuario']

    def Quantidade(self, obj):
        return obj.get_quantidade()

    def get_licenca_usuario(self, obj):
        return obj.get_usuario()
    get_licenca_usuario.short_description = 'Usuários'


class CustoAdmin(admin.ModelAdmin):
    fields = ('licenca',)
    list_display = ('Licenca', 'total_unitario',)
    list_filter = ('licenca',)
    filter_vertical = ['licenca']
    autocomplete_fields = ('licenca',)

    def Licenca(self, obj):
        return obj.get_licenca()

    def total_unitario(self, obj):
        return obj.get_total_unitario()

    total_unitario.short_description = 'Total Unitário'


admin.site.register(Licenca, LicencaAdmin)
admin.site.register(Custo, CustoAdmin)
