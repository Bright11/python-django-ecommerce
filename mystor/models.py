import imp
from operator import mod
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
from distutils.command.upload import upload #for upoading image
from turtle import tilt, title
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200, null=True, blank=True)
    joined_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    
class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products')
    mared_price=models.PositiveIntegerField()
    salling_price=models.PositiveIntegerField()
    description=models.TextField()
    warranty=models.CharField(max_length=300,null=True,blank=True)
    return_policy=models.CharField(max_length=300,null=True,blank=True)
    view_count=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    customer=models.ForeignKey(
        Customer, on_delete=models.SET_NULL,null=True,blank=True
    )
    total=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Cart: '+str(self.id)
    
class CartProduct(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product, on_delete=models.CASCADE)
    rate=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    subtotal=models.PositiveIntegerField()
    
    def __str__(self):
        return 'Cart: ' + str(self.cart.id) + 'CartProduct: ' + str(self.id)
    
ORDER_STATUS= (
    ('Order Received','Order Received'),
    ('Order Processing','Order Received'),
    ('On the way','On the way'),
    ('Order Completed','Order Completed'),
    ('Order Canceled','Order Canceled'),
)

class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by=models.CharField(max_length=200)
    shiping_address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(null=True,blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    order_status=models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Order: ' + str(self.id)
    
    
#after creating of models, we need to run migration
#if image is among, install pillow
#pip install pillow
#python manage.py makemigrations
#python manage.py migrate
#Now go admin.py to register it
#in admin.py, import our models
#eg, from .models import *
#admin.register([Models name,another models name])