from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Courses.models import Course

def profile_pic(instance,filename:str):
    extension=filename.split('.')[1]
    return f'Profile_images/{instance.user}.{extension}'

def docs(instance,filename:str):
    extension=filename.split('.')[1]
    return f'documents/{instance.user}.{extension}'

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20)
    image=models.ImageField(upload_to=profile_pic, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    @receiver(post_save, sender=User)
    def create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return str(self.user)
    

class Application(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
    phone=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    document=models.FileField( upload_to=docs, max_length=100)
    class Meta:
        verbose_name = ("Application")
        verbose_name_plural = ("Applications")

    def __str__(self):
        return str(self.user)
    


    

