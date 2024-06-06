from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'user_images/{instance.user}.{extension}'

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to=user_image)
    phone=models.CharField(max_length=15)
    

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    @receiver(post_save, sender=User)
    def create_proifile(sender, instance ,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    

    def __str__(self):
        return str(self.user)

    
