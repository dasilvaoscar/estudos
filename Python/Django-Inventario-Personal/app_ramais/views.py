from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
# Create your views here.

class RamaisView(ListView):
    form_class = RamalForm

    def get(self, request):
        form = RamalForm()
        object_list = Telefone.objects.all()
        return render(request, 'app_ramais/ramais_tables.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = Telefone.objects.all()
        form = RamalForm(request.POST)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_ramais/ramais_tables.html', {'form': form, 'object_list': object_list}) 
    
class RamaisUpdateView(UpdateView):   
    model = Telefone
    form_class = RamalForm
    template_name = 'app_ramais/ramais_tables.html'
    success_url = reverse_lazy('ramais')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Telefone.objects.all()
        return context
    
class RamaisDeleteView(DeleteView):
    model = Telefone
    success_url = reverse_lazy('ramais')
    template_name = 'app_ramais/ramais_tables.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = ImageUpload.objects.all()
        context["form"] = RamalForm()
        return context