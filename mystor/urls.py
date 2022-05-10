from importlib.resources import path
from django.urls import path
#from . import views
from .views import *
from .models import *

app_name="mystor"

urlpatterns = [
    #path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('cart/',CartView.as_view(),name='cart'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('allproduct/',AllproductView.as_view(),name='allproduct'),
    path('product/<slug:slug>',ProductDetailsView.as_view(),name='productdetails'),
    
    path('add-to-cart-<int:pro_id>/',AddToCartView.as_view(),name='addtocart'),
    path('mycart/',MyCartView.as_view(),name='mycart'),
    path('deleteandupdatecart/<int:cp_id>/',DeleteandupdatecartView.as_view(),name='deleteandupdatecart'),
   path('emptycart',EmptyCartView.as_view(),name='emptycart'),
]
