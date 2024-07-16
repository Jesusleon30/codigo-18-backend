from rest_framework import serializers
from .models import CategoriaModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel

        # solo se puede usar uno de los dos: 

        # que campos queremos utilizar:
        fields = '__all__' # con esto le decimos que me valide todo

        # que campos queremos excluir:
        # exclude = ['id']


