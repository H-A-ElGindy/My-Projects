from django.db import models
from django.utils.text import slugify


type=(("Months", "Months"),("Weeks", "Weeks"),("Days", "Days"),)
levels=(("Beginner","Beginner"),("Intermediate","Intermediate"),("Advanced","Advanced"),)

def course_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'course_image/{instance.slug}.{extension}'
  
class Course (models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,blank=True,null=True)
    level=models.CharField(max_length=50,choices=levels)
    Duration=models.IntegerField()
    duration_type=models.CharField(max_length=50,choices=type)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to=course_image)
    created_at=models.DateTimeField(auto_now=True)
    is_available=models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Course,self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return str(self.name)

    
