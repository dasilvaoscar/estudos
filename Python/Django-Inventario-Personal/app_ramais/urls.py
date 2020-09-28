from django.urls import path
from app_inventario.views import *
from .views import *

urlpatterns = [
  path('', RamaisView.as_view(), name="ramais"),
  path('Update/<int:pk>', RamaisUpdateView.as_view(), name='ramais_update'),
  path('Delete/<int:pk>', RamaisDeleteView.as_view(), name='ramais_delete'),
  
]
