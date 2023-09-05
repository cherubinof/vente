from django.urls import path
from ecomme import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('shop',views.shop,name='shop'),
    path('filter-data',views.filter_data,name='filter-data'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    
    #error page
    path('error404',views.error404,name='error404'),
    
    #account
    path('login/',views.LOGIN,name='login'),
    path('register',views.register,name='register'),
    # path('logout',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile',views.profile,name='profile'),
    path('profile/update',views.profile_update,name='profile_update'),
    
]