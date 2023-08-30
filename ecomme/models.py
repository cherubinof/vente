from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.


TYPE_TITRE = {
    ('Bonne_affaire','Bonne_affaire'),
    ('Nouvelle_arrivage','Nouvelle_arrivage')
}
class Slider(models.Model):
    titre = models.CharField(max_length=100,choices=TYPE_TITRE)
    texte = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/slider_img')
    

class Pub(models.Model):
    rabais = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/pub_img')


class Banner(models.Model):
    noms = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/banner_img')
    
    def __str__(self):
        return self.noms

class Main_category(models.Model):
    noms = models.CharField(max_length=100)
    
    def __str__(self):
        return self.noms

class Categorie(models.Model):
    Main_category = models.ForeignKey(Main_category,on_delete=models.CASCADE)
    noms = models.CharField(max_length=100)
    
    def __str__(self):
        return self.noms

class Sub_category(models.Model):
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    noms = models.CharField(max_length=100)


class Section(models.Model):
    noms = models.CharField(max_length=100)
    
    def __str__(self):
        return self.noms


class Produit(models.Model):
    quantite_total = models.IntegerField()
    disponibilite = models.IntegerField()
    images = models.ImageField(upload_to='produit/produit_img')
    nom_produit = models.CharField(max_length=100)
    prix = models.IntegerField()
    rabais = models.IntegerField()
    info_produit = RichTextField(null=True)
    nom_model = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)
    description = RichTextField()
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nom_produit
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("", kwargs={'slug':self.slug})
    
    class Meta:
        db_table = "ecomme_produit"
   

def create_slug(instance, new_slug=None):
    slug = slugify(instance.nom_produit)
    if new_slug is not None:
        slug = new_slug
    qs = Produit.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug ="%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receive(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receive, Produit)


class Produit_Image(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produit/prod_img')
    

class Information_suplementaire(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)