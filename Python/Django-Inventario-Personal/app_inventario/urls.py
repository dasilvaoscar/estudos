from django.urls import path
from app_inventario.views import *
from .import views

urlpatterns = [
  
  #Computadores
  path('Computadores/', ComputerView.as_view(), name='computadores'),
  path('Computadores/<int:pk>/Update/', ComputerUpdateView.as_view(), name='computadores_update'),
  path('Computadores/<int:pk>/Delete/', ComputerDeleteView.as_view(), name='computadores_delete'),
  path('Relatorio_De_Alocacao/', RelatorioAlocacao.as_view(), name="relatorioAlocacao_url"),

  #Access Point
  path('AP/', APView.as_view(), name='accesspoint'),
  path('AP/<int:pk>/Update/', APUpdateView.as_view(), name='accesspoint_update'),
  path('AP/<int:pk>/Delete/', APDeleteView.as_view(), name='accesspoint_delete'),


  #Anti-Malware
  path('Anti-Malware/', AntiMalwareView.as_view(), name='antivirus'),
  path('Anti-Malware/<int:pk>/Update/', AntiMalwareUpdateView.as_view(), name='antivirus_update'),
  path('Anti-Malware/<int:pk>/Delete/', AntiMalwareDeleteView.as_view(), name='antivirus_delete'),
#
  ##Câmeras
  path('Cam/', CamView.as_view(), name='cameras'),
  path('Cam/<int:pk>/Update/', CamUpdateView.as_view(), name='cameras_update'),
  path('Cam/<int:pk>/Delete/', CamDeleteView.as_view(), name='cameras_delete'),
#
  ##Dispositivos de Rede
  path('DDR/', DDRView.as_view(), name='ddr'),
  path('DDR/<int:pk>/Update/', DDRUpdateView.as_view(), name='ddr_update'),
  path('DRR/<int:pk>/Delete/', DDRDeleteView.as_view(), name='ddr_delete'),
#
  ##Impressoras
  path('IMP/', ImpressorasView.as_view(), name='impressoras'),
  path('IMP/<int:pk>/Update/', ImpressorasUpdateView.as_view(), name='impressoras_update'),
  path('IMP/<int:pk>/Delete/', ImpressorasDeleteView.as_view(), name='impressoras_delete'),
#
  ##Switches
  path('SW/', SwitchesView.as_view(), name='switches'),
  path('SW/<int:pk>/Update/', SwitchesUpdateView.as_view(), name='switches_update'),
  path('SW/<int:pk>/Delete/', SwitchesDeleteView.as_view(), name='switches_delete'),

]
