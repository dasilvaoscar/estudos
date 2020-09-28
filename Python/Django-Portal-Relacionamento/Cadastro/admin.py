from django.contrib import admin

# Register your models here.
from Cadastro.models import CNT, ATI, Anexos

admin.site.register(ATI)
admin.site.register(CNT)
admin.site.register(Anexos)