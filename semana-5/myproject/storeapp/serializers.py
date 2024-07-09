from rest_framework.serializers import ModelSerializer
from .models import Product, Category

# luego de importar ambas clases podemos crear nuestra clase serializer
class ProductSerializer(ModelSerializer):
    class Meta:
        #paso 1:  definir el modelo que usara este serializer 
        model = Product
        #paso2: definir cuales son los campos que quiero usar del modelo
        # '__all__' =  es igual a decir que vamos usar todos los campos del modelo 
        fields = '__all__'  


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'