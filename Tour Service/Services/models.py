from email import charset
from django.db import models
from django.forms import ImageField
from django.utils.text import slugify

class Category (models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,null=True,blank=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_available=models.BooleanField(default=True)
    

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


def guide_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'guide_images/{instance.name}.{extension}'

class Travel_Guide(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to=guide_image, height_field=None, width_field=None, max_length=None)
    created_at=models.DateTimeField(auto_now_add=True)
    is_available=models.BooleanField(default=True)
    
    class Meta:
        verbose_name = ("Travel_Guide")
        verbose_name_plural = ("Travel_Guides")

    def __str__(self):
        return self.name


def tour_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'tour_images/{instance.slug}.{extension}'

class Continent(models.Model):
    name=models.CharField(max_length=50)
    slug= slug=models.SlugField(unique=True,null=True,blank=True)
    class Meta:
        verbose_name = ("Continent")
        verbose_name_plural = ("Continents")
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Continent,self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    continent=models.ForeignKey(Continent, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    slug= slug=models.SlugField(unique=True,null=True,blank=True)
    class Meta:
        verbose_name = ("Counrty")
        verbose_name_plural = ("Countries")

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Country,self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tour(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    continent=models.ForeignKey(Continent,  on_delete=models.CASCADE)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    travel_guide=models.ForeignKey(Travel_Guide, on_delete=models.CASCADE)
    city=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,null=True,blank=True)
    description=models.TextField()
    days=models.IntegerField()
    persons=models.IntegerField()
    price=models.IntegerField()
    offer_price=models.IntegerField(blank=True,null=True)
    offer_percent=models.IntegerField(blank=True,null=True)
    image=models.ImageField( upload_to=tour_image, height_field=None, width_field=None, max_length=None)
    created_at=models.DateTimeField(auto_now_add=True)
    is_available=models.BooleanField(default=True)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.city)
        super(Tour,self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Tour")
        verbose_name_plural = ("Tours")

    def __str__(self):
        return self.city
    
class Offer(models.Model):
    tour=models.ForeignKey(Tour,on_delete=models.CASCADE)
    percent=models.IntegerField()

    def offer_price(self):
        final_price=self.tour.price-((self.tour.price*self.percent)/100)
        return final_price

    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return str(self.tour)

    


