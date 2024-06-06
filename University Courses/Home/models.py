from django.db import models


class Existing_Student(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('Existing_Student')
        verbose_name_plural = ('Existing Students')

    def __str__(self):
        return self.name
  

class Succes_Student(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Succes_Student")
        verbose_name_plural = ("Succes_Student")

    def __str__(self):
        return self.name

class New_Student(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('New_Student')
        verbose_name_plural = ('New_Students')

    def __str__(self):
        return self.name
    
class Current_Teacher(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('Current_Teacher')
        verbose_name_plural = ('Current_Teachers')

    def __str__(self):
        return self.name

class Award(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ('Award')
        verbose_name_plural = ('Awards')

    def __str__(self):
        return self.name
    
  

