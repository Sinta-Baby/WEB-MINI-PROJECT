from django.db import models

# Create your models here.
class Breeddb(models.Model):
    Breed_name =models.CharField(max_length=100,null=True,blank=True)
    Alpha_name =models.CharField(max_length=100,null=True,blank=True)
    Description =models.CharField(max_length=3000,null=True,blank=True)
    Health =models.CharField(max_length=3000,null=True,blank=True)
    Training =models.CharField(max_length=3000,null=True,blank=True)
    Exercise =models.CharField(max_length=3000,null=True,blank=True)
    breed_image =models.ImageField(upload_to="Breed images",null=True,blank=True)
