from django.http import *
from django.shortcuts import render
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.models import *
import pandas as pd
import pandas.io.sql as psql
import pymysql
#from app_custom.conn_db import Conexao

class RelatorioAlocacao(View):
        
    def get(self, request):
        form = ComputadorForm
        object_list = Computador.objects.filter(locado='L')
        for model in object_list:
            if model.locado=='L':
                model.locado ='SIM'
            else:
                model.locado ='NÃO'
        return render(request, 'app_inventario/maquinas_locadas.html', {'form': form, 'object_list': object_list})


# Access Points
class APView(ListView):
    form_class = ApForm

    def get(self, request):
        form = ApForm
        object_list = AccessPoint.objects.all()
        return render(request, 'app_inventario/access_point_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = AccessPoint.objects.all()
        form = ApForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/access_point_tables.html', {'form': form, 'object_list': object_list})

class APUpdateView(UpdateView):   
    model = AccessPoint
    form_class = ApForm
    template_name = 'app_inventario/access_point_tables.html'
    success_url = reverse_lazy('accesspoint')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = AccessPoint.objects.all()
        return context
    
class APDeleteView(DeleteView):
    model = AccessPoint
    success_url = reverse_lazy('accesspoint')
    template_name = 'app_inventario/access_point_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = AccessPoint.objects.all()
        context["form"] = APForm()
        return context

# Anti-Vírus
class AntiMalwareView(ListView):
    form_class = AntivirusForm

    def get(self, request):
        form = AntivirusForm
        object_list = Antivirus.objects.all()
        return render(request, 'app_inventario/anti_malware_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = Antivirus.objects.all()
        form = AntivirusForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/anti_malware_tables.html', {'form': form, 'object_list': object_list})

class AntiMalwareUpdateView(UpdateView):   
    model = Antivirus
    form_class = AntivirusForm
    template_name = 'app_inventario/anti_malware_tables.html'
    success_url = reverse_lazy('antivirus')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Antivirus.objects.all()
        return context
    
class AntiMalwareDeleteView(DeleteView):
    model = Antivirus
    success_url = reverse_lazy('antivirus')
    template_name = 'app_inventario/anti_malware_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Antivirus.objects.all()
        context["form"] = AntivirusForm()
        return context

# Computadores
class ComputerView(View):
    form_class = ComputadorForm

    def get(self, request):
        form = ComputadorForm
        object_list = Computador.objects.all()
        return render(request, 'app_inventario/computer_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = Computador.objects.all()
        form = ComputadorForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/computer_tables.html', {'form': form, 'object_list': object_list})

class ComputerUpdateView(UpdateView):   
    model = Computador
    form_class = ComputadorForm
    template_name = 'app_inventario/computer_tables.html'
    success_url = reverse_lazy('computadores')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Computador.objects.all()
        return context
    
class ComputerDeleteView(DeleteView):
    model = Computador
    success_url = reverse_lazy('computadores')
    template_name = 'app_inventario/computador_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Computador.objects.all()
        context["form"] = CardapioForm()
        return context

# Câmeras
class CamView(ListView):
    form_class = CameraForm

    def get(self, request):
        form = CameraForm
        object_list = Camera.objects.all()
        return render(request, 'app_inventario/cameras_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = Camera.objects.all()
        form = CameraForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/cameras_tables.html', {'form': form, 'object_list': object_list})

class CamUpdateView(UpdateView):   
    model = Camera
    form_class = CameraForm
    template_name = 'app_inventario/cameras_tables.html'
    success_url = reverse_lazy('cameras')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Camera.objects.all()
        return context
    
class CamDeleteView(DeleteView):
    model = Camera
    success_url = reverse_lazy('cameras')
    template_name = 'app_inventario/cameras_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Camera.objects.all()
        context["form"] = CameraForm()
        return context

# Dispositivos de Rede
class DDRView(ListView):
    form_class = DDRForm

    def get(self, request):
        form = DDRForm
        object_list = DispositivosDeRede.objects.all()
        return render(request, 'app_inventario/ddr_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = DispositivosDeRede.objects.all()
        form = DDRForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/ddr_tables.html', {'form': form, 'object_list': object_list})

class DDRUpdateView(UpdateView):   
    model = DispositivosDeRede
    form_class = DDRForm
    template_name = 'app_inventario/ddr_tables.html'
    success_url = reverse_lazy('ddr')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = DispositivosDeRede.objects.all()
        return context
    
class DDRDeleteView(DeleteView):
    model = DispositivosDeRede
    success_url = reverse_lazy('ddr')
    template_name = 'app_inventario/ddr_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = DispositivosDeRede.objects.all()
        context["form"] = DDRForm()
        return context

# Impressoras
class ImpressorasView(ListView):
    form_class = ImpressorasForm

    def get(self, request):
        form = ImpressorasForm
        object_list = Impressora.objects.all()
        return render(request, 'app_inventario/impressoras_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = Impressora.objects.all()
        form = ImpressorasForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/impressoras_tables.html', {'form': form, 'object_list': object_list})

class ImpressorasUpdateView(UpdateView):   
    model = Impressora
    form_class = ImpressorasForm
    template_name = 'app_inventario/impressoras_tables.html'
    success_url = reverse_lazy('impressoras')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Impressora.objects.all()
        return context
    
class ImpressorasDeleteView(DeleteView):
    model = Impressora
    success_url = reverse_lazy('impressoras')
    template_name = 'app_inventario/impressoras_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Impressora.objects.all()
        context["form"] = ImpressorasForm()
        return context

# Switches
class SwitchesView(ListView):
    form_class = SwitchForm

    def get(self, request):
        form = SwitchForm
        object_list = Switch.objects.all()
        return render(request, 'app_inventario/switches_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = Switch.objects.all()
        form = SwitchForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_inventario/switches_tables.html', {'form': form, 'object_list': object_list})

class SwitchesUpdateView(UpdateView):   
    model = Switch
    form_class = SwitchForm
    template_name = 'app_inventario/switches_tables.html'
    success_url = reverse_lazy('switches')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Switch.objects.all()
        return context
    
class SwitchesDeleteView(DeleteView):
    model = Switch
    success_url = reverse_lazy('switches')
    template_name = 'app_inventario/switches_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Switch.objects.all()
        context["form"] = SwitchForm()
        return context
''' Caso preciso exportar para EXCEL
class RelatorioAlocacao(View, Conexao):
    def get(self, request):
        self.query = 'SELECT * FROM v_invent_computador'
        
        try:
            df = self.CreateConnection()
        except:
            return HttpResponse('Erro na criação da conexão')
        
        try:
            response = HttpResponse(content_type='text/xlsx')
        except Exception as e:
            raise Http404('Erro ao criar content type \n', e)
        
        try:
            response['Content-Disposition'] = 'attachment; filename="Máquinas alocadas.xlsx"'
        except Exception as e:
            raise Http404('Erro ao criar arquivo\n', e)
        
        try:
            df.to_excel(response, index=False)
            return response
        except Exception as e:
            raise Http404('Erro ao exportar \n', e)    
'''