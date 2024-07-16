from rest_framework import generics
from models import CategoriaModel
from .serializers import CategoriaSerializer
from rest_framework import response
from rest_framework import status

class CaterogiaApiView(generics.ListCreateAPIView):
    # SELECT * FROM categorias;
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer

class UnaCategoriaApiView(generics.RetrieveAPIView):
    def get(self, request, id):
        print(id)
        # SELECT * FROM categorias WHERE id=...;
        resultado = CategoriaModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
            'message': 'la categoria no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriaSerializer(instance=resultado)

        return response.Response(data={
            'message': serializer.data
        }, status=status.HTTP_200_OK)