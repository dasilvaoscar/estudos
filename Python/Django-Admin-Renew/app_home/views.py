from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.apps import config, apps
from django.contrib import admin

# Create your views here.

class HomePageView(View):
        
    def get(self, request):
        return render(request, 'app_home/index.html')
