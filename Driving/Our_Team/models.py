from django.db import models


def team_image(instance,filename:str):
    extension=filename.split('.')[1]
    return f'team_image/{instance.name}.{extension}'
class Team(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField( max_length=50)
    image=models.ImageField(upload_to=team_image, )

    class Meta:
        verbose_name = ("Team")
        verbose_name_plural = ("Teams")

    def __str__(self):
        return self.name

    

