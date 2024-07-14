from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    #esto es una tupla osea que no es mutable
    # Permite crear un tupla con los campos que queremos mostrar en el admin 
    list_display = ('id', 'name', 'description', 'price', 'stock')
    # list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)


