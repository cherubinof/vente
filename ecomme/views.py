from django.shortcuts import render
from.models import *

# Create your views here.


def accueil(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    pub = Pub.objects.all().order_by('-id')[0:3]
    banner = Banner.objects.all()
    main_category = Main_category.objects.all()
    # categorie = Categorie.objects.all()
    # sub_category = Sub_category.objects.all()
    produit = Produit.objects.filter(section__noms = 'produit en vedette')
    product = Produit.objects.filter(section__noms ='recent')
    
    
    context = {
        'sliders':sliders,
        'pub':pub,
        'banner':banner,
        'main_category':main_category,
        # 'categorie':categorie,
        # 'sub_category':sub_category,
        'produit':produit,
        'product':product,
    }
    return render(request,'ecomme/accueil.html',context)


def detail(request,pk):
    produit = Produit.objects.get(pk=pk)
    produit_image = Produit_Image.objects.all()
    context = {
        'produit':produit,
        'produit_image':produit_image
    }
    return render(request,'ecomme/detail.html',context)

def shop(request):
    produits = Produit.objects.all()
    context = {
        'produits':produits
    }
    return render(request, 'ecomme/shop.html',context)

def cart(request):
    return render(request, 'ecomme/cart.html')

def checkout(request):
    return render(request, 'ecomme/checkout.html')

def contact(request):
    return render(request, 'ecomme/contact.html')
