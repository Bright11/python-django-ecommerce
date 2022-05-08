#from itertools import product
from re import template
from django.shortcuts import render

# Create your views here.
from urllib import request
from django.shortcuts import render
from django.conf import settings
#using template view
from django.views.generic import TemplateView
from .models import *

#def home(request):
 #   return render(request,'home.html')
 
 # 
class HomeView(TemplateView):
     template_name='home.html'
     
     def get_context_data(self, **kwargs):
          context= super().get_context_data(**kwargs)
          context['product_list']=Product.objects.all()
          context['allcategories']=Category.objects.all()
          return context
     
     
class AllproductView(TemplateView):
     template_name='allproduct.html'
     
     def get_context_data(self, **kwargs):
          context =super().get_context_data(**kwargs)
          context['allcategories']=Category.objects.all()
          return context
          
    
class AboutView(TemplateView):
    template_name='about.html'
    
    
    
    
class CartView(TemplateView):
     template_name='cart.html'
     
     
class ContactView(TemplateView):
     template_name='contact_us.html'
    
    
 