from django.contrib import admin
from .models import Contrato, Empresas, FormaPagamento
ModelAdmin = admin.ModelAdmin


class ContratoInline(admin.TabularInline):
    can_delete = True
    model = Contrato
    extra = 1

    fieldsets = [
        (None, {'fields': ['t_empresa', 'servico', 'forma_de_pagamento',
                           'dt_lancamento', 'valor_contrato']}),
    ]


class EmpresaAdmin(ModelAdmin):

    fieldsets = [
        ('EMPRESA', {'fields': ['nome'], 'classes': ['extrapretty']}),
    ]
    inlines = [ContratoInline]

    # if necessary add def total by Empresa
    # readonly_fields = ['total']

    # add def total if necessary
    list_display = ['nome', ]

    def total(self, obj):
        return obj.get_total()


admin.site.register(Empresas, EmpresaAdmin)
admin.site.register(FormaPagamento)





