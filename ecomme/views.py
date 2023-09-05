from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

login_required(login_url='/login')
def detail(request,pk):
    produit = Produit.objects.filter(pk=pk)
    produit_image = Produit_Image.objects.all()
    if produit.exists():
        produit = Produit.objects.get(pk=pk)
    else:
        return redirect('error404')
    context = {
        'produit':produit,
        'produit_image':produit_image
    }
    return render(request,'ecomme/detail.html',context)


def shop(request):
    produits = Produit.objects.all()
    categorie = Categorie.objects.all()
    context = {
        'produits':produits,
        'categorie':categorie
    }
    return render(request, 'ecomme/shop.html',context)

def filter_data(request):
    categorie = request.GET.getlist('categorie[]')
    brands = request.GET.gestlist('brand[]')
    
    allproduit = Produit.objects.all().order_by('-id').distinct()
    if len(categorie) > 0:
        allproduit = allproduit.filter(brand__id__in=brands).distinct()
    
    t = render_to_string('ajax/produit-list.html', {'produit':allproduit})
    return JsonResponse({'data': t})

def cart(request):
    return render(request, 'ecomme/cart.html')

def checkout(request):
    return render(request, 'ecomme/checkout.html')



def contact(request):
    return render(request, 'ecomme/contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'ce noms existe deja')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'email exite deja')
            return redirect('register')
        
        
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    else:
        return render(request,'registration/register.html')
    

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            messages.error(request,'noms et mot de pass inccorect')
            return redirect('login')
    return render(request,'registration/login.html')


def profile(request):
    return render(request,'account/profile.html')

def profile_update(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        quartier = request.POST.get('quartier')
        zipcode = request.POST.get('zipcode')
        user_id = request.user.id
        
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.username = username
        user.email = email
        user.mobile = mobile
        user.address1 = address1
        user.address2 = address2
        user.pays = pays
        user.ville = ville
        user.quartier = quartier
        user.zipcode = zipcode
        
        user.save()
        messages.success(request,'profile modifier avec success')
        return redirect('profile')
        
        

def error404(request):
    return render(request,'error/404.html')
