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
        print (CategoriaModel.objects.filter(id = id))
        CategoriaModel.objects.filter(id = id).first()
        return response.Response(data={
            'message': 'ok'
        }, status=status.HTTP_200_OK)