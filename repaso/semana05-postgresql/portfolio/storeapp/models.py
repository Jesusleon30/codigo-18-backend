from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'






class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0) # este no puede ser negativo
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    # blank=True, null=True estos son importantes que sean aa true sino nos puede pedir que 
    # haguemos un reinicio completo 
    
    image = models.TextField(null=True, blank=True)
    # se crea de forma automatica son solo de lectura no modificables
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    # de esta forma le pongo el nombre de la tabla
    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'products' 

