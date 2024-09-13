from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.utils.text import slugify
# rest frame work token imports 
from django.conf import settings
from rest_framework.authtoken.models import Token


# signal to create auth token automatically in api
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def profile_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'profile_images/{instance.profile_slug}.{extension}'


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    profile_slug=models.SlugField(unique=True,blank=True,null=True)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    facebook=models.URLField(max_length=2000,unique=True,null=True,blank=True)
    linkedin=models.URLField(max_length=2000,unique=True,null=True,blank=True)
    role=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=11,unique=True,null=True,blank=True) # 11 for egypt mobile numbers
    designation=models.CharField(max_length=50,null=True,blank=True)
    rating_total=models.DecimalField(max_digits=1, decimal_places=1,null=True,blank=True)
    rating_number=models.IntegerField(null=True,blank=True)
    average_rating=models.DecimalField(max_digits=1, decimal_places=1,null=True,blank=True)
    image=models.ImageField(upload_to=profile_image,null=True,blank=True)
    biography=models.TextField(null=True,blank=True)
    joined_at=models.DateTimeField(auto_now_add=True) 
    is_available=models.BooleanField(default=True)
    def save(self,*args, **kwargs):
        self.profile_slug=slugify(self.user)
        super(Profile,self).save(*args, **kwargs)
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
    @receiver(post_save, sender=User)
    def create_profile(instance,created,sender, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    def __str__(self):
        return str(self.user)


def post_file(instance,filename:str):
    extension=filename.split('.')[1]
    return f'post_files/{instance.profile}.{extension}'


class Post(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    post_slug=models.SlugField(blank=True,null=True)
    file=models.FileField(upload_to=post_file, max_length=100,null=True,blank=True)
    def file_tag(self):
        if self.file:
            return mark_safe('<img src="{}" height="50"/>'.format(self.file.url))
    description= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def save(self,*args, **kwargs):
        self.post_slug=slugify(self.title)
        super(Post,self).save(*args, **kwargs)
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
    def __str__(self):
        return str(self.profile)


