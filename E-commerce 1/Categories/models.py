from django.db import models
from django.utils.text import slugify

def category_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'category_images/{instance.slug}.{extension}'

# Create your models here.
class Category(models.Model):
    name=models.CharField( max_length=50,unique=True)
    slug=models.SlugField(unique=True,blank=True,null=True)
    image=models.ImageField( upload_to=category_image, height_field=None, width_field=None, max_length=None)
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

 