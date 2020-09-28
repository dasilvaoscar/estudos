from django.contrib import admin
from .models import *

@admin.register(Computador)
class ComputadorAdmin(admin.ModelAdmin):
    fields = ('nome', 'usuario', 'status', 'modelo', 'patrimonio', 'antivirus', 'tipo', 'locado')
    list_display = ('nome', 'usuario', 'status', 'modelo', 'patrimonio', 'antivirus', 'tipo', 'locado')
    list_filter = ('nome', 'usuario', 'status', 'modelo', 'patrimonio', 'antivirus', 'tipo', 'locado')
    search_fields = ('nome', 'usuario__username', 'status__status', 'modelo__modelo', 'patrimonio', 'antivirus__antivirus', 'tipo__tipo', 'locado')
    autocomplete_fields = ('antivirus', 'usuario',)

    empty_value_display = '-empty-'

@admin.register(Antivirus)
class AntivirusAdmin(admin.ModelAdmin):
    fields = ('antivirus', 'versao')
    list_display = ('antivirus', 'versao')
    list_filter = ('antivirus', 'versao')
    search_fields = ('antivirus', 'versao')
    search_fields = ('tipo',)

@admin.register(Modelo)
class AntivirusAdmin(admin.ModelAdmin):
    fields = ('modelo',)
    list_display = ('modelo',)
    list_filter = ('modelo',)
    search_fields = ('modelo',)


@admin.register(AccessPoint)
class AccessPointAdmin(admin.ModelAdmin):
    fields = ('nome', 'modelo', 'conf', 'mac_address')
    list_display = ('nome', 'modelo', 'conf', 'mac_address')
    list_filter = ('nome', 'modelo', 'conf', 'mac_address')
    search_fields = ('nome', 'modelo__id', 'conf', 'mac_address')

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    fields = ('nome', 'modelo', 'serial', 'ip')
    list_display = ('nome', 'modelo', 'serial', 'ip')
    list_filter = ('nome', 'modelo', 'serial', 'ip')
    serch_fields = ('nome', 'modelo__id', 'serial', 'ip')

@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    fields = ('nome', 'modelo', 'serial', 'ip')
    list_display = ('nome', 'modelo', 'serial', 'ip')
    list_filter = ('nome', 'modelo', 'serial', 'ip')
    search_fields = ('nome', 'modelo__id', 'serial', 'ip')

@admin.register(DispositivosDeRede)
class DispositivosDeRedeAdmin(admin.ModelAdmin):
    fields = ('nome', 'modelo', 'status', 'tipo',)
    list_display = ('nome', 'modelo', 'status', 'tipo',)
    list_filter = ('nome', 'modelo', 'status', 'tipo',)
    search_fields = ('nome', 'modelo__id', 'status__id', 'tipo__id',)

@admin.register(Impressora)
class ImpressoraAdmin(admin.ModelAdmin):
    fields = ('nome','modelo', 'status', 'ip',)
    list_display = ('nome','modelo', 'status', 'ip',)
    list_filter = ('nome','modelo', 'status', 'ip',)
    search_fields = ('nome','modelo__id', 'status__id', 'ip',)
