from django.db import models
from django.utils.text import slugify
from django.urls import reverse




def catimage(instance,filename:str):
    extension=filename.split('.')[1]
    return f'cat_images/{instance.category_slug}.{extension}'


def subimage(instance,filename:str):
    extension=filename.split('.')[1]
    return f'sub_images/{instance.sub_slug}.{extension}'

def proimage(instance,filename:str):
    extension=filename.split('.')[1]
    return f'pro_images/{instance.pro_slug}.{extension}'

class Category (models.Model):
    category_name=models.CharField( max_length=50)
    category_slug=models.SlugField(unique=True,null=True,blank=True)
    image=models.ImageField(upload_to=catimage, height_field=None, width_field=None, max_length=None)
    created_at=models.DateTimeField( auto_now=True)


    def save(self,*args, **kwargs):
        self.category_slug=slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def get_url(self):
        return reverse("store:sub_category", args=[self.category_slug])

    def __str__(self):
        return self.category_name
    

class Sub_Category(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_name=models.CharField( max_length=50)
    sub_slug=models.SlugField(unique=True,null=True,blank=True)
    sub_image=models.ImageField(upload_to=subimage)
    created_at=models.DateTimeField(auto_now=True)
    

    def save(self,*args, **kwargs):
        self.sub_slug=slugify(self.sub_name)
        super(Sub_Category,self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = ("Sub_Category")
        verbose_name_plural = ("Sub_Categories")

    def get_url(self):
        return reverse("store:products", args=[self.category.category_slug,self.sub_slug])

    def __str__(self):
        return self.sub_name
    
    
    
class Product(models.Model):
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    pro_name=models.CharField(max_length=50)
    pro_slug=models.SlugField(unique=True,null=True,blank=True)
    pro_stock=models.IntegerField()
    pro_price=models.FloatField()
    pro_description=models.TextField()
    pro_image=models.ImageField(upload_to=proimage,)
    pro_offer_price=models.FloatField(null=True,blank=True)
    pro_offer_percent=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def save(self,*args, **kwargs):
        self.pro_slug=slugify(self.pro_name)
        super(Product,self).save(*args, **kwargs)

    def get_url(self):
        return reverse("store:product_detail", args=[self.sub_category.category.category_slug,self.sub_category.sub_slug,self.pro_slug])


    def __str__(self):
        return self.pro_name

class Offer(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    offer_percent=models.IntegerField()
    is_active=models.BooleanField()
    created_at=models.DateTimeField(auto_now=True)

    def offer_price(self):
        final_price=self.product.pro_price-((self.product.pro_price*self.offer_percent)/100)
        return final_price

    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
   


