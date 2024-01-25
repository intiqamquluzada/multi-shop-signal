from django.urls import path
from my_app.views import *



urlpatterns = [

path('cart/',cart_view,name = 'cart'),
path('checkout/',checkout_view,name = 'checkout'),
path('contact/',contact_view,name = 'contact'),
path('detail/<slug>/',detail_view,name = 'detail'),
path('index/',index_view,name = 'index'),
path('shop/',shop_view,name = 'shop'),


]