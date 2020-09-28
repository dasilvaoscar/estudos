from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import LayoutMenssageContact
# Create your views here.

class HomePageView(ListView):
    template_name = 'app_home_page/index.html'
    queryset = LayoutMenssageContact.objects.all()

    
    def get_queryset(self):
        return LayoutMenssageContact.objects.order_by('-data')[:1]