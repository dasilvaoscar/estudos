from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
# Create your views here.

class CardapioIndexView(View):   
    form_class = CardapioForm

    def get(self, request):
        form = CardapioForm()
        object_list = ImageUpload.objects.all()
        return render(request, 'app_cardapio/cardapio_index.html', {'form': form, 'object_list': object_list})        

    def post(self, request):
        object_list = ImageUpload.objects.all()
        form = CardapioForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

        return render(request, 'app_cardapio/cardapio_index.html', {'form': form, 'object_list': object_list}) 
    

class CardapioUpdateView(UpdateView):   
    model = ImageUpload
    form_class = CardapioForm
    template_name = 'app_cardapio/cardapio_index.html'
    success_url = reverse_lazy('cardapio')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = ImageUpload.objects.all()
        return context
    
class CardapioDeleteView(DeleteView):
    model = ImageUpload
    success_url = reverse_lazy('cardapio')
    template_name = 'app_cardapio/cardapio_index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = ImageUpload.objects.all()
        context["form"] = CardapioForm()
        return context