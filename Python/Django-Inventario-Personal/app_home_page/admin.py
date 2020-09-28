from django.contrib import admin
from .models import LayoutMenssagePresentation, LayoutMenssageContact, LayoutEmail
# Register your models here.

admin.site.register(LayoutEmail)
admin.site.register(LayoutMenssageContact)
admin.site.register(LayoutMenssagePresentation)
