#from itertools import product
from itertools import product
from multiprocessing import context
from queue import Empty
from re import template
from django import views
from django.shortcuts import redirect, render

# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
from django.conf import settings
#using template view
from django.views.generic import TemplateView
from .models import *
from django.shortcuts import get_object_or_404

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
     
     #getting product and its categories
class AllproductView(TemplateView):
     template_name='allproduct.html'
     
     def get_context_data(self, **kwargs):
          context =super().get_context_data(**kwargs)
          context['allcategories']=Category.objects.all().order_by('-id')
          return context
          
#product details
class ProductDetailsView(TemplateView):
     template_name='productdetails.html'
     
     def get_context_data(self, **kwargs):
          context= super().get_context_data(**kwargs)
          slug= kwargs['slug']
          #print(slug, '99999999999999999')
          url_slug= self.kwargs['slug']
          product= Product.objects.get(slug=url_slug)
          product.view_count += 1 #view count
          product.save() #view count save
          context['product']=product
          return context
    
    
#add to crat
class AddToCartView(TemplateView):
     template_name='addtocart.html'
     
     def get_context_data(self, **kwargs):
          context= super().get_context_data(**kwargs)
          #getting product id from requested url
          product_id= self.kwargs['pro_id']
          #print(product_id, '*************')
          #get product
          product_obj=Product.objects.get(id=product_id)
          
          #check if product exeis
          cart_id = self.request.session.get('cart_id',None)
          if cart_id:
               cart_obj= Cart.objects.get(id=cart_id)
               #print('old cart')
               this_object_in_cart=cart_obj.cartproduct_set.filter(
                    product=product_obj
               )
               #if item already exist
               if this_object_in_cart.exists():
                    cartproduct=this_object_in_cart.last()
                    cartproduct.quantity +=1
                    cartproduct.subtotal += product_obj.salling_price
                    cartproduct.save()
                    cart_obj.total += product_obj.salling_price
                    cart_obj.save()
                    #if new item is add to the cart
               else:
                    cartproduct=CartProduct.objects.create(
                         cart=cart_obj,product=product_obj,rate=product_obj.salling_price,quantity=1
                         ,subtotal=product_obj.salling_price
                    )
                    cart_obj.total += product_obj.salling_price
                    cart_obj.save()
          else:
               cart_obj=Cart.objects.create(total=0)
               self.request.session['cart_id']=cart_obj.id
               cartproduct=CartProduct.objects.create(
                         cart=cart_obj,product=product_obj,rate=product_obj.salling_price,quantity=1
                         ,subtotal=product_obj.salling_price
                    )
               cart_obj.total += product_obj.salling_price
               cart_obj.save()
          return context
         
         
                #print('new cart')
               
#view cart page
class MyCartView(TemplateView):
     template_name='mycart.html'
     
     def get_context_data(self, **kwargs):
          context= super().get_context_data(**kwargs)
          cart_id= self.request.session.get('cart_id',None)
          if cart_id:
               cart=Cart.objects.get(id=cart_id)
          else:
               cart=None
          context['cart'] = cart
          return context
          
     
class DeleteandupdatecartView(views.View):
     def get(self, request, *args, **kwargs):
          print('this is manage cart')
          cp_id= self.kwargs['cp_id']
          action = request.GET.get('action')
          cp_obj = CartProduct.objects.get(id=cp_id)
          cart_obj= cp_obj.cart
         # print(cp_id,action)
          if action == 'inc':
               cp_obj.quantity += 1
               cp_obj.subtotal += cp_obj.rate
               cp_obj.save()
               cart_obj.total += cp_obj.rate
               cart_obj.save()
          elif action == 'dcr':
               cp_obj.quantity -= 1
               cp_obj.subtotal -= cp_obj.rate
               cp_obj.save()
               cart_obj.total -= cp_obj.rate
               cart_obj.save()
               if cp_obj.quantity ==0:
                    cp_obj.delete()
          elif action == 'remv':
               cart_obj.total -= cp_obj.subtotal
               cart_obj.save()
               cp_obj.delete()
          else:
               pass
          return redirect('mystor:mycart')

#empty cart code
class EmptyCartView(views.View):
     def get(self,request,*args, **kwargs):
          cart_id = request.session.get('cart_id', None)
          if cart_id:
               cart= Cart.objects.get(id=cart_id)
               cart.cartproduct_set.all().delete()
               cart.total =0
               cart.save()
          return redirect('mystor:mycart')

class AboutView(TemplateView):
    template_name='about.html'
    
    
    
    
class CartView(TemplateView):
     template_name='cart.html'
     
     
class ContactView(TemplateView):
     template_name='contact_us.html'
    
    
 