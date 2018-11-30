from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# Create your views here.

class HomePage(ListView):

    #queryset = 
    template_name = 'home.html'
