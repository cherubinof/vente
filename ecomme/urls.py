from django.urls import path
from ecomme import views

urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('shop',views.shop,name='shop'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact')
]