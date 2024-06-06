from django.db import models
from django.utils.text import slugify

def meeting_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'meetings/{instance.slug}.{extension}'

class Meeting(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,blank=True,null=True)
    date=models.DateField( auto_now_add=False)
    description=models.TextField()
    price=models.IntegerField()
    Hours_1=models.CharField(max_length=50)
    Hours_2=models.CharField(max_length=50)
    location_1=models.CharField(max_length=50)
    location_2=models.CharField(max_length=50)
    book_1=models.CharField(max_length=50)
    book_2=models.CharField(max_length=50)
    image=models.ImageField( upload_to=meeting_image)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Meeting,self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Meeting")
        verbose_name_plural = ("Meetings")

    def __str__(self):
        return self.title

