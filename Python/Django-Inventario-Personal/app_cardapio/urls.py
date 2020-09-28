from django.urls import path
from .views import *

urlpatterns = [
    path('', CardapioIndexView.as_view(), name='cardapio'),
    path('Update/<int:pk>', CardapioUpdateView.as_view(), name='cardapio_update'),
    path('Delete/<int:pk>', CardapioDeleteView.as_view(), name='cardapio_delete'),
]