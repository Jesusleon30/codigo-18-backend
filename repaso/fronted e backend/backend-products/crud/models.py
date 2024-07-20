from django.db import models

# Create your models here.

class ProductModel(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()


# en la terminal estoy ejecutando 
# python manage.py makemigrations
# python manage.py migrate