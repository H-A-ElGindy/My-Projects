
from django.db import models
from django.utils.text import slugify

def Course_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'Course_images/{instance.slug}.{extension}'

class Course(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,blank=True,null=True)
    date=models.DateField( auto_now_add=False)
    description=models.TextField()
    price=models.IntegerField()
    Hours=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    book=models.CharField(max_length=50)
    image=models.ImageField( upload_to=Course_image)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Course,self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title