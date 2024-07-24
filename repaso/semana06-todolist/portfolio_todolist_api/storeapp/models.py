from django.db import models
from tasks.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0) # este no puede ser negativo
    is_active = models.BooleanField(default=True)
    # category = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(
         Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='productos/', blank=True, null=True)
    # se crea de forma automatica son solo de lectura no modificables
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    # de esta forma le pongo el nombre de la tabla
    # def __str__ (self) -> str:
    #     return self.name

    class Meta:
        db_table = 'products' 

