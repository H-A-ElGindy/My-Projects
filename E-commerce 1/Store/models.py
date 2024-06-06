from pyexpat import model
from django.db import models
from Categories.models import Category
from django.utils.text import slugify
from django.urls import reverse


def Product_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'Product_image/{instance.slug}.{extension}'
# Create your models here.
class Product(models.Model):
    name=models.CharField( max_length=50,unique=True)
    slug=models.SlugField(unique=True,blank=True,null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to=Product_image, height_field=None, width_field=None, max_length=None)
    stock=models.IntegerField()
    price=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_available=models.BooleanField(default=True)
    offerprice=models.IntegerField(null=True,blank=True)
    offerpercent=models.IntegerField(null=True,blank=True)

    
    def save (self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args, **kwargs)

    def get_url(self):
        return reverse("store:detail", args=[self.category.slug,self.slug])
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

class Offer(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    percent=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def offer_price(self):
        final_price=(self.product.price - ((self.product.price*self.percent)/100))
        return final_price

    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return str(self.product)


  

    
  
