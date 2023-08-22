from django.contrib import admin
from.models import *

# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    list_display = ['titre','texte']
admin.site.register(Slider,SliderAdmin)

class PubAdmin(admin.ModelAdmin):
    list_display = ['rabais']
admin.site.register(Pub,PubAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['noms']
admin.site.register(Banner,BannerAdmin)

class Main_CategoryAdmin(admin.ModelAdmin):
    list_display = ['noms']
admin.site.register(Main_category,Main_CategoryAdmin)


admin.site.register(Categorie)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['noms']
admin.site.register(Sub_category,SubCategoryAdmin)

class Produit_images(admin.TabularInline):
    model = Produit_Image

class Informations_suplementaires(admin.TabularInline):
    model = Information_suplementaire

class ProduitAdmin(admin.ModelAdmin):
    inlines = (Produit_images, Informations_suplementaires)
    list_display = ['nom_produit', 'prix', 'categorie', 'section']
    list_editable = ['categorie', 'section']

admin.site.register(Section)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Produit_Image)
admin.site.register(Information_suplementaire)



