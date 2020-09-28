from django.contrib import admin
from .models import Estoque




class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'descricao', 'quantidade')
    list_filter = ('equipamento', 'descricao', 'quantidade')
    search_fields = ('equipamento', 'descricao', 'quantidade')
    actions = ['add', 'remove']

    fieldsets = [
        ('Descrições', {'fields': [('equipamento', 'descricao') ], 'classes': ['extrapretty']}),
        ('Valores', {'fields': ['quantidade'], 'classes': ['extrapretty']}),
    ]

    def add(modeladmin, request, queryset): 
        for estoque in queryset:
            estoque.quantidade = estoque.quantidade + 1 
            estoque.save()
    add.short_description = "Adicionar"

    def remove(modeladmin, request, queryset):
        for estoque in queryset:
            estoque.quantidade = estoque.quantidade - 1 
            estoque.save()
    remove.short_description = "Remover"


admin.site.register(Estoque, EstoqueAdmin)