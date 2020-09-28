from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
import adminactions.actions as actions


urlpatterns = [

    path('jet/', include('jet.urls', 'jet')), # Sempre permanecer no top
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('adminactions/', include('adminactions.urls')),
    path('', include('app_home_page.urls')),
    path('inventario/', include('app_inventario.urls')),
    path('ramais/', include('app_ramais.urls')),
    path('cardapio/', include('app_cardapio.urls')),
    re_path(r'^adminactions/', include('adminactions.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

actions.add_to_site(site)

admin.site.site_header = 'Inventário'
admin.site.index_title = 'Menu de Administração Intranet'
admin.site.site_title = 'Seja Bem Vindo!'